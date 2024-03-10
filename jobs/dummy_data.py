# Inside your_app_name/management/commands/generate_dummy_data.py
import os ,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.core.management.base import BaseCommand
from faker import Faker
from django.utils import timezone
from job.models import Job, JobApply
from django.utils.text import slugify

fake = Faker()

class Command(BaseCommand):
    help = 'Generate dummy data for Job and JobApply models'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Generating dummy data...'))

        for _ in range(10):  # Adjust the number of records as needed
            title = fake.job()
            description = fake.text()
            job_type = fake.random_element(elements=('Internship', 'PartTime', 'Fulltime', 'Contract'))
            education = fake.random_element(elements=('PHD', 'Master', 'Bachelor'))
            experience = fake.random_element(elements=('NoExperience', 'Junior', 'MidLevel', 'MidSenior'))
            salary = fake.random_int(min=30000, max=100000)
            position = fake.job()
            due_date = fake.date_this_year(after_today=True)
            created_at = fake.date_time_this_decade()
            user = fake.random_int(min=1, max=100)
            email = fake.email()
            company = fake.company()

            job = Job.objects.create(
                title=title,
                description=description,
                job_type=job_type,
                education=education,
                experience=experience,
                salary=salary,
                position=position,
                due_date=due_date,
                created_at=created_at,
                user=user,
                email=email,
                company=company,
                slug=slugify(title)
            )

            for _ in range(3):  # Create 3 JobApply records for each Job
                user_id = fake.random_int(min=1, max=100)
                resume = fake.file_name()
                cover_letter = fake.text(max_nb_chars=500)
                applied_at = fake.date_time_this_decade()

                JobApply.objects.create(
                    user=user_id,
                    job=job,
                    resume=resume,
                    cover_letter=cover_letter,
                    applied_at=applied_at
                )
        self.stdout.write(self.style.SUCCESS('Dummy data generation completed.'))
    
    
