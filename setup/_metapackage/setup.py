import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-crm",
    description="Meta package for oca-crm Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-crm_lead_code',
        'odoo14-addon-crm_lead_firstname',
        'odoo14-addon-crm_lead_vat',
        'odoo14-addon-crm_phonecall',
        'odoo14-addon-crm_security_group',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
