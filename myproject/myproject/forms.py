""" Docs. """

from shop2.forms.checkout import CustomerForm as CustomerFormBase


class CustomerForm(CustomerFormBase):
    """ docs. """
    field_order = ['salutation', 'first_name', 'last_name', 'email']
