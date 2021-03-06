# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aklub', '0021_auto_20160623_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewUser',
            fields=[
            ],
            options={
                'verbose_name_plural': 'new users',
                'proxy': True,
                'verbose_name': 'new user',
            },
            bases=('aklub.userincampaign',),
        ),
        migrations.CreateModel(
            name='UserYearPayments',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Payments for users in time periods',
                'proxy': True,
                'verbose_name': 'Payment for users in time period',
            },
            bases=('aklub.userincampaign',),
        ),
        migrations.AlterModelOptions(
            name='userincampaign',
            options={'ordering': ('surname', 'firstname'), 'verbose_name': 'User in campaign', 'verbose_name_plural': 'Users in campaign'},
        ),
        migrations.AlterField(
            model_name='terminalcondition',
            name='variable',
            field=models.CharField(blank=True, choices=[('UserInCampaign.active', 'UserInCampaign Aktivní: BooleanField '), ('UserInCampaign.activity_points', 'UserInCampaign Body za aktivitu: IntegerField '), ('UserInCampaign.additional_information', 'UserInCampaign Rozšiřující informace: TextField '), ('UserInCampaign.addressment', 'UserInCampaign Oslovení v dopise: CharField '), ('UserInCampaign.addressment_on_envelope', 'UserInCampaign Oslovení na obálku: CharField '), ('UserInCampaign.city', 'UserInCampaign Město/Městská část: CharField '), ('UserInCampaign.club_card_available', 'UserInCampaign Nárok na klubovou kartu: BooleanField '), ('UserInCampaign.club_card_dispatched', 'UserInCampaign Klubová karta odeslána?: BooleanField '), ('UserInCampaign.country', 'UserInCampaign Země: CharField '), ('UserInCampaign.different_correspondence_address', 'UserInCampaign Jiná korespondenční adresa: BooleanField '), ('UserInCampaign.email', 'UserInCampaign Email: CharField '), ('UserInCampaign.exceptional_membership', 'UserInCampaign Výjimečné členství: BooleanField '), ('UserInCampaign.expected_date_of_first_payment', 'UserInCampaign Očekávané datum první platby: DateField '), ('UserInCampaign.expected_regular_payment_date', 'UserInCampaign expected regular payment date: DateField '), ('UserInCampaign.extra_money', 'UserInCampaign extra money: IntegerField '), ('UserInCampaign.field_of_work', 'UserInCampaign Pracovní oblast: CharField '), ('UserInCampaign.firstname', 'UserInCampaign Jméno: CharField '), ('UserInCampaign.id', 'UserInCampaign ID: AutoField '), ('UserInCampaign.knows_us_from', 'UserInCampaign Odkud nás zná?: CharField '), ('UserInCampaign.language', "UserInCampaign Jazyk: CharField ('cs', 'en')"), ('UserInCampaign.last_payment', 'UserInCampaign last payment: DenormDBField '), ('UserInCampaign.no_upgrade', 'UserInCampaign no upgrade: NullBooleanField '), ('UserInCampaign.note', 'UserInCampaign Poznámka pro oživení nudného formuláře: TextField '), ('UserInCampaign.number_of_payments', 'UserInCampaign number of payments: IntegerField '), ('UserInCampaign.old_account', 'UserInCampaign Starý účet: BooleanField '), ('UserInCampaign.other_benefits', 'UserInCampaign Další benefity: TextField '), ('UserInCampaign.other_support', 'UserInCampaign Jiná podpora: TextField '), ('UserInCampaign.payment_total', 'UserInCampaign payment total: FloatField '), ('UserInCampaign.profile_picture', 'UserInCampaign Profilová fotografie: FileField '), ('UserInCampaign.profile_text', 'UserInCampaign A jaký je Tvůj důvod?: TextField '), ('UserInCampaign.public', 'UserInCampaign Zveřejnit mé jméno v seznamu podporovatelů: BooleanField '), ('UserInCampaign.recruiter', 'UserInCampaign recruiter: ForeignKey '), ('UserInCampaign.registered_support', 'UserInCampaign Registrace podpory: DateTimeField '), ('UserInCampaign.regular_amount', 'UserInCampaign Částka pravidelné platby: PositiveIntegerField '), ('UserInCampaign.regular_frequency', "UserInCampaign Frekvence pravidelných plateb: CharField ('monthly', 'quaterly', 'biannually', 'annually')"), ('UserInCampaign.regular_payments', 'UserInCampaign Pravidelné platby: BooleanField '), ('UserInCampaign.sex', "UserInCampaign Pohlaví: CharField ('male', 'female', 'unknown')"), ('UserInCampaign.source', 'UserInCampaign Zdroj: ForeignKey '), ('UserInCampaign.street', 'UserInCampaign Ulice a číslo domu (č.p./č.o.): CharField '), ('UserInCampaign.surname', 'UserInCampaign Příjmení: CharField '), ('UserInCampaign.telephone', 'UserInCampaign Telefon: CharField '), ('UserInCampaign.title_after', 'UserInCampaign Titul za jménem: CharField '), ('UserInCampaign.title_before', 'UserInCampaign Titul před jménem: CharField '), ('UserInCampaign.variable_symbol', 'UserInCampaign Variabilní symbol: CharField '), ('UserInCampaign.verified', 'UserInCampaign Ověřen: BooleanField '), ('UserInCampaign.verified_by', 'UserInCampaign Ověřil: ForeignKey '), ('UserInCampaign.why_supports', 'UserInCampaign Proč nás podporuje?: TextField '), ('UserInCampaign.wished_information', 'UserInCampaign Zasílat pravidelné informace emailem: BooleanField '), ('UserInCampaign.wished_tax_confirmation', 'UserInCampaign Zaslat daňové potvrzení (na konci roku): BooleanField '), ('UserInCampaign.wished_welcome_letter', 'UserInCampaign Odeslat uvítací dopis s členskou kartou: BooleanField '), ('UserInCampaign.zip_code', 'UserInCampaign PSČ: CharField '), ('UserInCampaign.last_payment.BIC', 'UserInCampaign.last_payment BIC: CharField '), ('UserInCampaign.last_payment.KS', 'UserInCampaign.last_payment KS: CharField '), ('UserInCampaign.last_payment.SS', 'UserInCampaign.last_payment SS: CharField '), ('UserInCampaign.last_payment.VS', 'UserInCampaign.last_payment VS: CharField '), ('UserInCampaign.last_payment.account', 'UserInCampaign.last_payment Account: CharField '), ('UserInCampaign.last_payment.account_name', 'UserInCampaign.last_payment Jméno účtu: CharField '), ('UserInCampaign.last_payment.account_statement', 'UserInCampaign.last_payment account statement: ForeignKey '), ('UserInCampaign.last_payment.amount', 'UserInCampaign.last_payment Částka: PositiveIntegerField '), ('UserInCampaign.last_payment.bank_code', 'UserInCampaign.last_payment Kód banky: CharField '), ('UserInCampaign.last_payment.bank_name', 'UserInCampaign.last_payment Jméno banky: CharField '), ('UserInCampaign.last_payment.currency', 'UserInCampaign.last_payment Currency: CharField '), ('UserInCampaign.last_payment.date', 'UserInCampaign.last_payment Datum platby: DateField '), ('UserInCampaign.last_payment.done_by', 'UserInCampaign.last_payment Provedl: CharField '), ('UserInCampaign.last_payment.id', 'UserInCampaign.last_payment ID: AutoField '), ('UserInCampaign.last_payment.operation_id', 'UserInCampaign.last_payment Operation ID: CharField '), ('UserInCampaign.last_payment.order_id', 'UserInCampaign.last_payment Order ID: CharField '), ('UserInCampaign.last_payment.recipient_message', 'UserInCampaign.last_payment Recipient message: CharField '), ('UserInCampaign.last_payment.specification', 'UserInCampaign.last_payment Specification: CharField '), ('UserInCampaign.last_payment.transfer_note', 'UserInCampaign.last_payment Transfer note: CharField '), ('UserInCampaign.last_payment.transfer_type', 'UserInCampaign.last_payment Transfer type: CharField '), ('UserInCampaign.last_payment.type', "UserInCampaign.last_payment Typ: CharField ('bank-transfer', 'cash', 'expected', 'darujme')"), ('UserInCampaign.last_payment.user', 'UserInCampaign.last_payment user: ForeignKey '), ('UserInCampaign.last_payment.user_identification', 'UserInCampaign.last_payment Identifikace odesílatele: CharField '), ('UserInCampaign.source.direct_dialogue', 'UserInCampaign.source Pochází z Direct dialogu: BooleanField '), ('UserInCampaign.source.id', 'UserInCampaign.source ID: AutoField '), ('UserInCampaign.source.name', 'UserInCampaign.source Jméno: CharField '), ('UserInCampaign.source.slug', 'UserInCampaign.source Identifikátor: SlugField '), ('action', "Akce: CharField ('daily', 'new-user', 'new-payment')")], help_text='Value or variable on left-hand side', max_length=50, null=True, verbose_name='Variable'),
        ),
    ]
