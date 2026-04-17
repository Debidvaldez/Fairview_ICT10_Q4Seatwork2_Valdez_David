from pyscript import document

class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return f"{self.name} | {self.section} | {self.favorite_subject}"

classmates = [
    Classmate("Annika", "Sapphire", "English"),
    Classmate("Uno", "Sapphire", "Math"),
    Classmate("Michael", "Sapphire", "Science"),
    Classmate("Samantha", "Sapphire", "Science"),
    Classmate("David", "Sapphire", "Social Studies"),
]

list_visible = False

def render_list():
    body = document.getElementById("listBody")
    body.innerHTML = ""

    for c in classmates:
        row = document.createElement("tr")

        name_cell = document.createElement("td")
        name_cell.textContent = c.name

        section_cell = document.createElement("td")
        section_cell.textContent = c.section

        subject_cell = document.createElement("td")
        subject_cell.textContent = c.favorite_subject

        row.appendChild(name_cell)
        row.appendChild(section_cell)
        row.appendChild(subject_cell)

        body.appendChild(row)

def add_classmate(e):
    name = document.getElementById("nameInput").value.strip()
    section = document.getElementById("sectionInput").value.strip()
    subject = document.getElementById("subjectInput").value.strip()

    if name and section and subject:
        classmates.append(Classmate(name, section, subject))

        document.getElementById("nameInput").value = ""
        document.getElementById("sectionInput").value = ""
        document.getElementById("subjectInput").value = ""

        if list_visible:
            render_list()

def toggle_list(e):
    global list_visible

    container = document.getElementById("listContainer")
    button = e.target

    if list_visible:
        container.style.display = "none"
        button.textContent = "Show Classmates"
        list_visible = False
    else:
        render_list()
        container.style.display = "block"
        button.textContent = "Hide Classmates"
        list_visible = True