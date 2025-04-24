from faker import Faker

def generate_fake_data(seed=42):
    faker = Faker()
    faker.seed_instance(seed)
    return faker