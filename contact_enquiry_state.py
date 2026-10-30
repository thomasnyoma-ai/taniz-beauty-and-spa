import logging
import os
import re
from typing import Any

import httpx
import reflex as rx


class ContactEnquiryState(rx.State):
    email_form_connected: bool = bool(
        os.getenv("RESEND_API_KEY") and os.getenv("RESEND_FROM_EMAIL")
    )
    is_sending: bool = False
    feedback: str = ""
    send_succeeded: bool = False

    @rx.event
    def submit_enquiry(self, form_data: dict[str, Any]):
        name_value = form_data.get("name", "")
        email_value = form_data.get("email", "")
        enquiry_type_value = form_data.get("enquiry_type", "")
        message_value = form_data.get("message", "")

        name = name_value.strip() if isinstance(name_value, str) else ""
        email = email_value.strip() if isinstance(email_value, str) else ""
        enquiry_type = (
            enquiry_type_value.strip()
            if isinstance(enquiry_type_value, str)
            else ""
        )
        message = (
            message_value.strip() if isinstance(message_value, str) else ""
        )

        if not (2 <= len(name) <= 100):
            self.feedback = "Please enter a name between 2 and 100 characters."
            self.send_succeeded = False
            return
        if len(email) > 254 or not re.fullmatch(
            r"[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+)*@[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)+",
            email,
        ):
            self.feedback = "Please enter a valid email address."
            self.send_succeeded = False
            return
        if enquiry_type not in {"treatment", "visit"}:
            self.feedback = (
                "Please choose treatment or visit as your enquiry type."
            )
            self.send_succeeded = False
            return
        if not (10 <= len(message) <= 5000):
            self.feedback = (
                "Please enter a message between 10 and 5,000 characters."
            )
            self.send_succeeded = False
            return
        if not (os.getenv("RESEND_API_KEY") and os.getenv("RESEND_FROM_EMAIL")):
            self.feedback = (
                "Email form not connected yet — use WhatsApp or email for now."
            )
            self.send_succeeded = False
            return

        self.feedback = ""
        self.send_succeeded = False
        self.is_sending = True
        yield ContactEnquiryState.deliver_enquiry(
            name, email, enquiry_type, message
        )

    @rx.event(background=True)
    async def deliver_enquiry(
        self, name: str, email: str, enquiry_type: str, message: str
    ):
        api_key = os.getenv("RESEND_API_KEY", "")
        sender = os.getenv("RESEND_FROM_EMAIL", "")
        if not api_key or not sender:
            async with self:
                self.is_sending = False
                self.send_succeeded = False
                self.feedback = "Email form not connected yet — use WhatsApp or email for now."
            return

        payload = {
            "from": sender,
            "to": ["tanizbeautyandspa986@gmail.com"],
            "reply_to": email,
            "subject": f"Website {enquiry_type} enquiry from {name}",
            "text": (
                f"New {enquiry_type} enquiry from the Taniz Beauty & Spa website.\n\n"
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Enquiry type: {enquiry_type}\n\n"
                f"Message:\n{message}"
            ),
        }
        try:
            async with httpx.AsyncClient(timeout=20.0) as client:
                response = await client.post(
                    "https://api.resend.com/emails",
                    headers={
                        "Authorization": f"Bearer {api_key}",
                        "Content-Type": "application/json",
                    },
                    json=payload,
                )
                response.raise_for_status()
                response_data = response.json()
                if not isinstance(response_data, dict) or not response_data.get(
                    "id"
                ):
                    raise ValueError(
                        "Email provider did not confirm acceptance"
                    )
        except Exception as e:
            logging.exception(f"Error: {e}")
            async with self:
                self.is_sending = False
                self.send_succeeded = False
                self.feedback = (
                    "We couldn't send your enquiry right now. Please use WhatsApp "
                    "or email Taniz directly using the contact links on this page."
                )
            return

        async with self:
            self.is_sending = False
            self.send_succeeded = True
            self.feedback = (
                "Your enquiry has been sent to Taniz. We’ll reply to the email "
                "address you provided."
            )
