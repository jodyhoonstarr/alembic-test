"""empty message

Revision ID: 72e8c6e2073a
Revises: 
Create Date: 2022-07-21 23:23:11.683299

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mssql

# revision identifiers, used by Alembic.
revision = '72e8c6e2073a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('API_BusinessPartners',
    sa.Column('ID', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('Authority_Fk', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('Agency_Fk', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('BP_Name', sa.VARCHAR(length=120, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('BP_Contact', sa.VARCHAR(length=80, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('BP_Phone', sa.VARCHAR(length=12, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('BP_Email', sa.VARCHAR(length=120, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('BP_Address', sa.VARCHAR(length=120, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('BP_City', sa.VARCHAR(length=120, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('BP_State', sa.VARCHAR(length=120, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('BP_Zip', sa.VARCHAR(length=10, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Outage_Email', sa.VARCHAR(length=120, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('Create_Date', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.Column('Create_User', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Update_User', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Update_Date', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('ID', name='PK__API_Busi__3214EC27E0308C86')
    )
    op.create_table('API_Metrics',
    sa.Column('ID', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('Authority_Fk', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('Service_Fk', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('BP_Fk', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('Create_Date', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.Column('Update_Date', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.Column('Number_of_Hits', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('ID', name='PK__API_Metr__3214EC27B95FD6A9')
    )
    op.create_table('API_Services',
    sa.Column('ID', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('Authority_Fk', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('Service_URL', sa.VARCHAR(length=240, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('Service_Description', sa.VARCHAR(length=120, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Service_JSON', sa.VARCHAR(length=1, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Service_XML', sa.VARCHAR(length=1, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Create_Date', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.Column('Create_User', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Update_User', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Update_Date', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('ID', name='PK__API_Serv__3214EC27CD40D416')
    )
    op.create_table('API_Subscriptions',
    sa.Column('ID', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('BP_Fk', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('Service_Fk', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('Application_Name', sa.VARCHAR(length=240, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('Usage_Description', sa.VARCHAR(length=240, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('Anticipated_Hits', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('Create_Date', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.Column('Create_User', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Update_User', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Update_Date', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.Column('SubscriptAPIKey', mssql.UNIQUEIDENTIFIER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('ID', name='PK__API_Subs__3214EC277D3B36BB')
    )
    op.create_table('Agencies',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('agency_name', sa.VARCHAR(length=120, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('address', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('city', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('state', sa.VARCHAR(length=2, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('zip', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('zip5', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=128, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('phone', sa.VARCHAR(length=15, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('giswebapp_fk', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('authority_fk', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('create_date', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.Column('create_user', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('update_user', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('update_date', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='PK__Agencies__3213E83F53CA1200')
    )
    op.create_table('AuthAdmins',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('User_Fk', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('Authority_Fk', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='PK_AuthAdmins')
    )
    op.create_table('Authorities',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('authname', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('auth_address', sa.VARCHAR(length=120, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('auth_city', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('auth_state', sa.VARCHAR(length=5, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('auth_zip', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('auth_zip5', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('endusers_fk', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('giswebapp_fk', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('a_locked', sa.VARCHAR(length=1, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('app_name', sa.VARCHAR(length=120, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('app_descr', sa.VARCHAR(length=240, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('authority_url', sa.VARCHAR(length=255, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('app_url', sa.VARCHAR(length=300, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('app_z_level', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('app_cent_lat', sa.NUMERIC(precision=10, scale=6), autoincrement=False, nullable=True),
    sa.Column('app_cent_lon', sa.NUMERIC(precision=10, scale=6), autoincrement=False, nullable=True),
    sa.Column('authcode', sa.VARCHAR(length=20, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('create_date', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.Column('create_user', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('locked_by', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('locked_date', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.Column('update_user', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('update_date', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='PK_Authorities')
    )
    op.create_table('Authority_MAR_Services',
    sa.Column('ID', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('Authid_Fk', sa.NUMERIC(precision=18, scale=0), autoincrement=False, nullable=False),
    sa.Column('Database_Type', sa.CHAR(length=1, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Url', sa.VARCHAR(length=300, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Db', sa.VARCHAR(length=40, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('DBSchema', sa.VARCHAR(length=40, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Credential_Key', sa.VARCHAR(length=100, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Usrname', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Pwd', sa.VARCHAR(length=20, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Update_User', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Update_Date', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.Column('Create_User', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Create_Date', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('ID', name='PK__Authorit__3214EC2763BDD845')
    )
    op.create_table('Authority_Mapdb_Services',
    sa.Column('ID', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('Authid_Fk', sa.NUMERIC(precision=18, scale=0), autoincrement=False, nullable=False),
    sa.Column('Database_Type', sa.CHAR(length=1, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('Url', sa.VARCHAR(length=300, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('DB', sa.VARCHAR(length=40, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('DBSchema', sa.VARCHAR(length=40, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Street_Srid', sa.NUMERIC(precision=18, scale=0), autoincrement=False, nullable=True),
    sa.Column('Address_Srid', sa.NUMERIC(precision=18, scale=0), autoincrement=False, nullable=True),
    sa.Column('Agency_Extents_Srid', sa.NUMERIC(precision=18, scale=0), autoincrement=False, nullable=True),
    sa.Column('Credential_Key', sa.VARCHAR(length=100, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Usrname', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Pwd', sa.VARCHAR(length=20, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Update_User', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Update_Date', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.Column('Create_User', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Create_Date', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.Column('F_Create_Usr_Col', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('F_Create_Date_Col', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('F_Updt_Usr_Col', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('F_Updt_Date_Col', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('ID', name='PK__Authorit__3214EC2726C0ED02')
    )
    op.create_table('GIS_App_Codes',
    sa.Column('ID', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('Application_Name', sa.NCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('Is_Desktop', sa.NCHAR(length=1), autoincrement=False, nullable=True),
    sa.Column('Description', sa.NCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('Update_User', sa.NCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('Update_Date', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.Column('Create_User', sa.NCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('Create_Date', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('ID', name='APP_CODE_PK')
    )
    op.create_table('GIS_Config_Variables',
    sa.Column('ID', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('GISDesktopApp_Fk', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('Config_Name', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Config_Value', sa.VARCHAR(length=120, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Config_Description', sa.VARCHAR(length=240, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Authority_Fk', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('Update_User', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Create_User', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Update_Date', sa.DATETIME(), server_default=sa.text('(getdate())'), autoincrement=False, nullable=True),
    sa.Column('Create_Date', sa.DATETIME(), server_default=sa.text('(getdate())'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('ID', name='CONFIG_VARIABLES_PK')
    )
    op.create_table('GIS_Default_Values',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('SW_FieldName', sa.VARCHAR(length=32, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('SW_Description', sa.VARCHAR(length=120, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('Default_Value', sa.VARCHAR(length=32, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Authority_Fk', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='PK_GIS_Default_Values')
    )
    op.create_table('GIS_DesktopLyrs',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('gisdesktopapp_fk', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('layer_descript', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('layer_name', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('layer_field', sa.VARCHAR(length=32, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('mar_table', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('mar_field', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('isaccess_lyr', sa.VARCHAR(length=1, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Authority_Fk', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='PK_GIS_DesktopLyrs')
    )
    op.create_table('GIS_FieldMapping',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('Authority_Fk', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('FeatureType', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('SW_FieldName', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('GIS_FieldName', sa.VARCHAR(length=32, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('FieldDataType', sa.VARCHAR(length=32, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('FieldDescription', sa.VARCHAR(length=240, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('View_FieldName', sa.VARCHAR(length=120, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('DesktopLyrs_Fk', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='PK_GIS_FieldMapping')
    )
    op.create_table('GIS_SubAddresses',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('FeatureTypeFk', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('FeatureType', sa.NVARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('Authority_Fk', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('IS_PARENT', sa.NVARCHAR(length=1), autoincrement=False, nullable=True),
    sa.Column('Description', sa.NVARCHAR(length=240), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='PK_GIS_SubAddresses')
    )
    op.create_table('GisWebAPP_Overlays',
    sa.Column('ID', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('Authority_Fk', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('Layer_Url', sa.VARCHAR(length=400, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Layer_Desc', sa.VARCHAR(length=255, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Layer_Seq', sa.NUMERIC(precision=10, scale=0), autoincrement=False, nullable=True),
    sa.Column('Isagency_Xtnts_Lyr', sa.VARCHAR(length=5, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Visible', sa.VARCHAR(length=5, collation='SQL_Latin1_General_CP1_CI_AS'), server_default=sa.text("('Y')"), autoincrement=False, nullable=True),
    sa.Column('Layer_Name', sa.VARCHAR(length=100, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Format', sa.VARCHAR(length=20, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Transparent', sa.VARCHAR(length=1, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Opacity', sa.NUMERIC(precision=18, scale=0), autoincrement=False, nullable=True),
    sa.Column('Service_Type', sa.VARCHAR(length=20, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Layer_Off', sa.VARCHAR(length=1, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Addresses', sa.CHAR(length=1, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Streets', sa.CHAR(length=1, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Layersrid', sa.NUMERIC(precision=18, scale=0), autoincrement=False, nullable=True),
    sa.Column('Color', sa.VARCHAR(length=30, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Width', sa.NUMERIC(precision=18, scale=0), autoincrement=False, nullable=True),
    sa.Column('Fillcolor', sa.VARCHAR(length=30, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Radius', sa.NUMERIC(precision=18, scale=0), autoincrement=False, nullable=True),
    sa.Column('Create_User', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Create_Date', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.Column('Update_User', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Update_Date', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.Column('DesktopLyrs_fk', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('Display_Name', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('ID', name='PK__GisWebAP__3214EC2743517675')
    )
    op.create_table('GisWebApp_Baselayers',
    sa.Column('ID', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('Authority_Fk', sa.NUMERIC(precision=18, scale=0), autoincrement=False, nullable=False),
    sa.Column('Layer_Desc', sa.VARCHAR(length=20, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Service_Type', sa.VARCHAR(length=50, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Layer_URL', sa.VARCHAR(length=255, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Visible', sa.VARCHAR(length=5, collation='SQL_Latin1_General_CP1_CI_AS'), server_default=sa.text("('Y')"), autoincrement=False, nullable=True),
    sa.Column('Layers', sa.VARCHAR(length=255, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Attribution', sa.VARCHAR(length=255, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Opacity', sa.NUMERIC(precision=18, scale=0), autoincrement=False, nullable=True),
    sa.Column('Layer_Seq', sa.NUMERIC(precision=18, scale=0), autoincrement=False, nullable=True),
    sa.Column('Create_User', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Create_Date', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.Column('Update_User', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Update_Date', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.Column('DIsplay_Name', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Layer_Name', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('ID', name='PK__GisWebAp__3214EC27CEAA0434')
    )
    op.create_table('Gisdesktop_Reporting',
    sa.Column('ID', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('App_Fk', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('Reporting_Type', sa.VARCHAR(length=240, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('View_Name', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('View_Fields', sa.VARCHAR(length=32, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('ID', name='PK__Gisdeskt__3214EC27F0D7803E')
    )
    op.create_table('Logins',
    sa.Column('ID', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('Usrname_Fk', sa.NUMERIC(precision=18, scale=0), autoincrement=False, nullable=False),
    sa.Column('Ondatetime', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.Column('Offdatetime', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.Column('Function_Fk', sa.NUMERIC(precision=18, scale=0), autoincrement=False, nullable=True),
    sa.Column('Ipaddress', sa.VARCHAR(length=20, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Returncode', sa.VARCHAR(length=20, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Usrname', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('ID', name='PK__Logins__3214EC27980E3AA7')
    )
    op.create_table('Mar_Maintenance_Status',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('Process_Date', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.Column('Completesubaddressfk', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('Addressfk', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('Process_Type', sa.VARCHAR(length=120, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Process_Status', sa.VARCHAR(length=32, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Solution', sa.VARCHAR(length=240, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='PK_Mar_Maintenance_Status')
    )
    op.create_table('Notification_Device',
    sa.Column('ID', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('Device_Type', sa.VARCHAR(length=32, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('ID', name='PK__Notifica__3214EC27BE470941')
    )
    op.create_table('Notification_Log',
    sa.Column('ID', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('Notif_Type', sa.NUMERIC(precision=18, scale=0), autoincrement=False, nullable=True),
    sa.Column('Sentdate', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.Column('Subject_Html', sa.VARCHAR(length=128, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Body_Html', sa.VARCHAR(length=3999, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Agency_Fk', sa.NUMERIC(precision=18, scale=0), autoincrement=False, nullable=True),
    sa.Column('Usrname_Fk', sa.NUMERIC(precision=18, scale=0), autoincrement=False, nullable=True),
    sa.Column('Read', sa.VARCHAR(length=1, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Num_Of_Attachments', sa.NUMERIC(precision=18, scale=0), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('ID', name='PK__Notifica__3214EC2742C8CEE8')
    )
    op.create_table('Notification_Types',
    sa.Column('ID', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('Notif_Type', sa.VARCHAR(length=32, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Notif_Limit', sa.NUMERIC(precision=18, scale=0), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('ID', name='PK__Notifica__3214EC279C0A8B55')
    )
    op.create_table('Notifications',
    sa.Column('ID', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('Agency_Fk', sa.NUMERIC(precision=18, scale=0), autoincrement=False, nullable=False),
    sa.Column('Usrname_Fk', sa.NUMERIC(precision=18, scale=0), autoincrement=False, nullable=False),
    sa.Column('Notification_Type_Fk', sa.NUMERIC(precision=18, scale=0), autoincrement=False, nullable=True),
    sa.Column('readaccepted', sa.VARCHAR(length=5, collation='SQL_Latin1_General_CP1_CI_AS'), server_default=sa.text("('False')"), autoincrement=False, nullable=False),
    sa.Column('message', sa.VARCHAR(length=3999, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('ID', name='PK__Notifica__3214EC2732E2F19D')
    )
    op.create_table('Users',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('usrname', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('usrname_address', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('usrname_city', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('usrname_state', sa.VARCHAR(length=2, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('usrname_zip', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('usrname_zip5', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('usrname_email', sa.VARCHAR(length=128, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('access_rights', sa.VARCHAR(length=1, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('agency_fk', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('authority_fk', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('isauthorityadmin', sa.VARCHAR(length=5, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('isagencyadmin', sa.VARCHAR(length=5, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('usrname_phone', sa.VARCHAR(length=14, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('usrname_cell', sa.VARCHAR(length=14, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('receive_notif', sa.VARCHAR(length=5, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('notif_only', sa.VARCHAR(length=1, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('usrname_full', sa.VARCHAR(length=90, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('notif_device_fk', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('usrname_domain', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('pwd', sa.VARCHAR(length=200, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('token', sa.VARCHAR(length=100, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('superuser', sa.VARCHAR(length=1, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('badlogins', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('tokendate', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.Column('userlocked', sa.VARCHAR(length=5, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('fname', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('lname', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('create_date', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.Column('create_user', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('update_user', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('update_date', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.Column('email_verified', sa.NCHAR(length=5), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='PK_Usersb')
    )
    op.create_table('UsersAgencies',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('agency_fk', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('usrid_fk', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('isagencyadmin', sa.VARCHAR(length=1, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('create_date', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.Column('create_user', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('authority_fk', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('isactivated', sa.VARCHAR(length=5, collation='SQL_Latin1_General_CP1_CI_AS'), server_default=sa.text("('False')"), autoincrement=False, nullable=True),
    sa.Column('land_developer', mssql.BIT(), server_default=sa.text('((0))'), autoincrement=False, nullable=True),
    sa.Column('standard_user', mssql.BIT(), server_default=sa.text('((0))'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='PK_UsersAgencies')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('UsersAgencies')
    op.drop_table('Users')
    op.drop_table('Notifications')
    op.drop_table('Notification_Types')
    op.drop_table('Notification_Log')
    op.drop_table('Notification_Device')
    op.drop_table('Mar_Maintenance_Status')
    op.drop_table('Logins')
    op.drop_table('Gisdesktop_Reporting')
    op.drop_table('GisWebApp_Baselayers')
    op.drop_table('GisWebAPP_Overlays')
    op.drop_table('GIS_SubAddresses')
    op.drop_table('GIS_FieldMapping')
    op.drop_table('GIS_DesktopLyrs')
    op.drop_table('GIS_Default_Values')
    op.drop_table('GIS_Config_Variables')
    op.drop_table('GIS_App_Codes')
    op.drop_table('Authority_Mapdb_Services')
    op.drop_table('Authority_MAR_Services')
    op.drop_table('Authorities')
    op.drop_table('AuthAdmins')
    op.drop_table('Agencies')
    op.drop_table('API_Subscriptions')
    op.drop_table('API_Services')
    op.drop_table('API_Metrics')
    op.drop_table('API_BusinessPartners')
    # ### end Alembic commands ###
