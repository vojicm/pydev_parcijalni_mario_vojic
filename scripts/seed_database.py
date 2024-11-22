from django.contrib.auth.models import User
from products.models import Product
from offers.models import Offer, OfferItem
from decimal import Decimal
from random import randint, choice
from datetime import datetime, timedelta

def run():
    # Create products
    if Product.objects.count() == 0:
        print("Seeding 50 products...")
        for i in range(1, 51):
            Product.objects.create(
                name=f"IT Product {i}",
                description=f"Description for IT Product {i}",
                price=Decimal(randint(100, 1000))
            )
        print("Products seeded successfully.")
    else:
        print("Products already exist, skipping seeding.")

    # Get superuser account
    superuser = User.objects.filter(is_superuser=True).first()
    if not superuser:
        print("Superuser account not found. Please create one first.")
        return

    # Create offers
    if Offer.objects.count() == 0:
        print("Seeding 15 offers...")
        products = list(Product.objects.all())
        for i in range(1, 16):
            offer_date = datetime.now() - timedelta(days=randint(1, 30))
            selected_products = [choice(products) for _ in range(randint(3, 7))]

            sub_total = sum(p.price for p in selected_products)
            tax = sub_total * Decimal("0.2")  # 20% tax
            total = sub_total + tax

            offer = Offer.objects.create(
                customer=superuser,
                date=offer_date.date(),
                sub_total=sub_total,
                tax=tax,
                total=total
            )

            for product in selected_products:
                OfferItem.objects.create(
                    offer=offer,
                    product=product,
                    quantity=randint(1, 3)
                )
        print("Offers seeded successfully.")
    else:
        print("Offers already exist, skipping seeding.")
