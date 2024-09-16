class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.__min_length = min_length
        self.__mails = mails
        self.__domains = domains

    def get_min_length(self):
        return self.__min_length
    def set_min_length(self, min_length):
        self.__min_length = min_length

    def get_mails(self):
        return self.__mails
    def set_mails(self, mails):
        self.__mails = mails

    def get_domains(self):
        return self.__domains
    def set_domains(self, domains):
        self.__domains = domains

   
    def __validate_name(self, name):
        return len(name) >= self.__min_length
    def __validate_mail(self, mail):
        return mail in self.__mails
    def __validate_domain(self, domain):
        return domain in self.__domains

  
    def validate(self, email):
        try:
            name, rest = email.split("@")
            mail, domain = rest.split(".")
        except ValueError:
            return False

        return (self.__validate_name(name) and
                self.__validate_mail(mail) and
                self.__validate_domain(domain))


# Example Usage
mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)

print(email_validator.validate("pe77er@gmail.com"))       
print(email_validator.validate("georgios@gmail.net"))      
print(email_validator.validate("stamatito@abv.net"))      
print(email_validator.validate("abv@softuni.bg"))          
