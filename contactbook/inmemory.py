from contact import Contact
from beautifultable import BeautifulTable



class InMemoryImp1:
    contacts = []
    
    @classmethod
    def addcontact(cls):
        name=input("enter the name")
        email=input("enter the email")
        mobile=input("enter the mobile")
        address=input("enter the address")
        cls.contacts.append(Contact(name,email,mobile,address))
        print("contact is added")

     
    @classmethod
    def deletecontact(cls):
        name = input("enter the name to delete:")
        contact = cls.get_contact_by_name(name)
        if contact:
            cls.contacts.remove(contact)
            print(f"contact(name) is deleted")
        else:
            print("contact (name) is not found")


    
    @classmethod
    def viewcontact(cls):
        InMemoryImp1._paint(cls.contacts)

    @classmethod
    def search(cls):
        if len(cls.contacts) > 0:
            name = input("enter the name to search:")
            s_list=list(filter(lambda x:name.lower() in x.get__name().lower(),cls.contacts))

            if len(s_list) > 0:
                InMemoryImp1._paint(s_list)
            else:
                print(f"no data is found")
        else:
            print("contact book is empty")


    @classmethod
    def update(cls):
        name = input("enter the name to be updated:")
        contact = cls.get_contact_by_name(name)
        if contact:
            print("1.new name 2.new email 3. new mobile 4.new address")
            ch=int(input("enter the choice:"))
            if ch==1:
                print(f"old name:{contact.get__name()}")
                name = input("enter the new name:")
                if name:
                    contact.set__name(name)
            elif ch==2:
                print(f"old email:{contact.get__email()}")
                email = input("enter the new email:")
                if email:
                    contact.set__email(email)
            elif ch==3:
                print(f"old mobil:{contact.get__mobile()}")
                mobile = input("enter the new mobile:")
                if mobile:
                    contact.set__mobile(mobile)
            else :
                print(f"old address:{contact.get__address()}")
                address = input("enter the new address:")
                if address:
                    contact.set__address(address)

    @staticmethod
    def _paint(lst):
        if len(lst) != 0:
            table=BeautifulTable()
            table.column_headers=["name","email","mobile","address"]
            for c in lst:
                table.append_row([c.get__name(),c.get__email(),c.get__mobile(),c.get__address()])
            print(table)
        else:
            print(f"contact book is empty")

    @classmethod
    def get_contact_by_name(cls,name):

        if len(cls.contacts) > 0:
            contact = list(filter(lambda x:x.get__name().lower() == name.lower(),cls.contacts))
            return contact [0] if contact else None