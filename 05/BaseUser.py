from dataclasses import dataclass , field
import uuid

@dataclass
class BaseUser:
    name: str
    email: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def display_info(self):
        return(
            f"ID: {self.id}\n"
            f"NAME: {self.name}\n"
            f"EMAIL: {self.email}"
        )

