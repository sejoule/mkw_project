# Generated by Django 2.0.6 on 2018-06-28 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tosca', '0003_auto_20180627_1744'),
    ]

    operations = [
        migrations.CreateModel(
            name='credential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protocol', models.CharField(max_length=1000, null=True)),
                ('token_type', models.CharField(default='password', max_length=1000)),
                ('token', models.CharField(default='', max_length=1000)),
                ('userh', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='scalar-unit.size',
            fields=[
                ('scalar-unit_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tosca.scalar-unit')),
            ],
            bases=('tosca.scalar-unit',),
        ),
        migrations.CreateModel(
            name='scalar-unit.time',
            fields=[
                ('scalar-unit_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tosca.scalar-unit')),
            ],
            bases=('tosca.scalar-unit',),
        ),
        migrations.CreateModel(
            name='tosca_datatypes_root',
            fields=[
                ('datatype_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tosca.DataType')),
            ],
            bases=('tosca.datatype',),
        ),
        migrations.AddField(
            model_name='artifactdefinition',
            name='deploy_path',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='artifactdefinition',
            name='file',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='artifactdefinition',
            name='repository',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='artifactdefinition',
            name='type',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='artifacttype',
            name='derived_from',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='artifacttype',
            name='mime_type',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='attributeassignment',
            name='attribute_name',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='attributedefinition',
            name='entry_schema',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='attributedefinition',
            name='status',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='attributedefinition',
            name='type',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='capabilitydefinition',
            name='type',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='capabilitytype',
            name='derived_from',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='datatype',
            name='derived_from',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='groupdefinition',
            name='type',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='grouptype',
            name='derived_from',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='importdefinition',
            name='file',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='importdefinition',
            name='namespace_prefix',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='importdefinition',
            name='namespace_uri',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='importdefinition',
            name='repository',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='interfacetype',
            name='derived_from',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='nodetemplate',
            name='type',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='nodetype',
            name='derived_from',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='operationdefinition',
            name='implementation',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='parameterdefinition',
            name='type',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='policydefinition',
            name='type',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='policytype',
            name='derived_from',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='propertyassignment',
            name='property_name',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='propertydefinition',
            name='entry_schema',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='propertydefinition',
            name='required',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='propertydefinition',
            name='status',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='propertydefinition',
            name='type',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='propertyfilterdefinition',
            name='property_name',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='relationshiptemplate',
            name='type',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='relationshiptype',
            name='derived_from',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='repositorydefinition',
            name='url',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='requirementassignment',
            name='capability',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='requirementassignment',
            name='node',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='requirementassignment',
            name='relationship',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='requirementdefinition',
            name='capability',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='requirementdefinition',
            name='node',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='requirementdefinition',
            name='relationship',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='servicetemplate',
            name='dsl_definitions',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='servicetemplate',
            name='tosca_definition_version',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='topologytemplate',
            name='substitution_mappings',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='artifactdefinition',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='artifacttype',
            name='description',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='attributedefinition',
            name='description',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='capabilitydefinition',
            name='description',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='capabilitytype',
            name='description',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='datatype',
            name='description',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='groupdefinition',
            name='description',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='grouptype',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='interfacetype',
            name='description',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='nodetemplate',
            name='description',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='nodetype',
            name='description',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='operationdefinition',
            name='description',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='policydefinition',
            name='description',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='policytype',
            name='description',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='propertydefinition',
            name='description',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='relationshiptemplate',
            name='description',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='relationshiptype',
            name='description',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='repositorydefinition',
            name='description',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='servicetemplate',
            name='description',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='value',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='topologytemplate',
            name='description',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='version',
            name='qualifier',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
