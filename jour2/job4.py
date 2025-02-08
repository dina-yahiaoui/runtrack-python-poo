class Student:
    def __init__(self, first_name, last_name, student_id):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_id = student_id
        self.__credits = 0
        self.__level = self.__student_eval()

    def add_credits(self, amount):
        if amount > 0:
            self.__credits += amount
            self.__level = self.__student_eval()
        else:
            print("Le nombre de crédits ajouté doit être supérieur à zéro.")

    def get_credits(self):
        return self.__credits

    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
    
    def student_info(self):
        print(f"Nom: {self.__last_name}, Prénom: {self.__first_name}, ID: {self.__student_id}, Niveau: {self.__level}")

# Instanciation de l'étudiant John Doe avec le numéro 145
student = Student("John", "Doe", 145)

# Ajout de crédits
student.add_credits(10)
student.add_credits(15)
student.add_credits(5)

# Affichage du total des crédits
total_credits = student.get_credits()
print(f"Total des crédits de John Doe: {total_credits}")

# Affichage des informations de l'étudiant
student.student_info()
