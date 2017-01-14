
class CompanySite(object):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.name = None  # *(String(50))
        self.addressLine1 = None  # (String(50))
        self.addressLine2 = None  # (String(50))
        self.city = None  # (String(50))
        self.state = None  # (String(50))
        self.zip = None  # (String(12))
        self.country = None  # (CountryReference)
        self.phoneNumber = None  # (String(30))
        self.faxNumber = None  # (String(30))
        self.taxCodeId = None  # (Integer)
        self.expenseReimbursement = None  # (Number)
        self.primaryAddressFlag = None  # (Boolean)
        self.defaultShippingFlag = None  # (Boolean)
        self.defaultBillingFlag = None  # (Boolean)
        self.defaultMailingFlag = None  # (Boolean)
        self.calendar = None  # (CalendarReference)
        self.timeZone = None  # (TimeZoneReference)
        self.company = None  # (CompanyReference)
        self._info = None  # (Metadata)
        
        # initialize object with json dict
        self.__dict__.update(json_dict)

    def __repr__(self):
        string = None
        string = ''.join('{}: {}\n'.format('Name',self.__dict__['name']))
        return string
