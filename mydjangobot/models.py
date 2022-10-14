from django.db import models

class DiscordUser(models.Model):
    discord_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=32)
    discriminator = models.CharField(max_length=4)

    def __str__(self):
        return f'{self.username}#{self.discriminator}'


class Debt(models.Model):
    debtor = models.ForeignKey(DiscordUser, on_delete=models.CASCADE, related_name='debtor')
    indebted = models.ForeignKey(DiscordUser, on_delete=models.CASCADE, related_name='indebted')
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    currency = models.CharField(max_length=32)
    start_date = models.DateField()
    due_date = models.DateField(null=True, blank=True)
    paid_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.indebted.username} le debe {self.amount} {self.currency} a {self.debtor.username}"
