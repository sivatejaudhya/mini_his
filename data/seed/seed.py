import random
from faker import Faker
from sqlalchemy.orm import Session
from backend.app.models.user import User
from backend.app.models.patient import Patient
from backend.app.core.db import Session, engine
from backend.app.core.security import hash_password


def seed_users(n=3):
    fake = Faker()
    roles = ["Admin", "Doctor", "Staff"]

    with Session(engine) as session:
        for _ in range(n):
            username = fake.user_name()
            email = fake.email()
            password = hash_password(fake.password(length=10))
            role = random.choice(roles)

            user = User(username=username, email=email, password=password, role=role)
            session.add(user)
        session.commit()

    print(f"Seeded {n} users successfully!")


def seed_patients(n=20):
    fake = Faker()

    with Session(engine) as session:
        for i in range(1, n + 1):
            name = fake.name()
            age = random.randint(0, 100)
            gender = random.choice(["Male", "Female", "Other"])
            contact = fake.phone_number()
            address = fake.address()
            medical_record_id = f"MR-{i:04d}"

            patient = Patient(
                name=name,
                age=age,
                gender=gender,
                contact=contact,
                address=address,
                medical_record_id=medical_record_id,
            )
            session.add(patient)
        session.commit()

    print(f"Seeded {n} patients successfully!")


if __name__ == "__main__":
    seed_users()
    seed_patients()
