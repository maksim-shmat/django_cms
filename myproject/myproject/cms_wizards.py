from django.utils.translation import ugettext_lazy as _
from cms.wizards.wizard_base import Wizard
from cms.wizards.wizard_pool import wizard_pool

from shop2.models.defaults.commodity import Commodity
from shop2.forms.wizards import CommodityWizardForm

commodity_wizard = Wizard(
    title=_("New Commodity"),
    weight=200,
    form=CommodityWizardForm,
    description=_("Create a new Commodity instance"),
    model=Commodity,
    template_name='shop2/wizards/create_product.html'
)
wizard_pool.register(commodity_wizard)
