# Generated by Django 3.2.4 on 2022-01-13 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_weight_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='casecbr',
            name='bmi',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='bt_qs1_chatxo',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='bt_qs1_nuoc',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='bt_qs1_vitamin_b12',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='bt_qs1_vitamin_d',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='bt_qs2_nuoc',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='bt_qs2_vitamin_b12',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='bt_qs2_vitamin_d',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='bt_qs3_nuoc',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='gender',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='name',
            field=models.TextField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='nc_qs1_chatbeo',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='nc_qs1_chatdam',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='nc_qs1_tinhbot',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='nc_qs1_vitamin_b12',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='nc_qs1_vitamin_d',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='nc_qs1_vitamin_e',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='nc_qs2_chatdam',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='nc_qs2_tinhbot',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='nc_qs2_vitamin_b12',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='nc_qs2_vitamin_d',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='result',
            field=models.TextField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='tc_qs1_chatbeo',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='tc_qs1_chatdam',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='tc_qs1_tinhbot',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='tc_qs1_vitamin_b12',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='tc_qs1_vitamin_d',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='tc_qs1_vitamin_e',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='tc_qs2_chatbeo',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='tc_qs2_chatdam',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='tc_qs2_tinhbot',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='tc_qs2_vitamin_b12',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='tc_qs2_vitamin_d',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='tdee_cungcap',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='tdee_thechat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='ts_cao_huyet_ap',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='ts_dai_thao_duong',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='ts_giam_tri_nho',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='ts_hen_xuyen',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='ts_parkinson',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='ts_viem_gan',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='casecbr',
            name='ts_xuong_khop',
            field=models.IntegerField(null=True),
        ),
    ]
