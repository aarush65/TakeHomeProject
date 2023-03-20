import unittest
class Project:
  def __init__(self) -> None:
     self.patients = {}
     self.exams = {}
     self.ans = []
  def open_file_and_process_input(self, file):
    with open(file, 'r') as f:
      line = f.readline()
      while line:
        stripped_line = line.strip()
        parsed_line = stripped_line.split(" ")        
        if parsed_line[0] == "ADD":
          patient_id = parsed_line[2]
          exam_id = parsed_line[3]
          if parsed_line[1] == "PATIENT":
              if patient_id not in self.patients:
                # If patient id does not already exist, adds a patient 
                # non_patient is the information in the line that does not include the patient's name
                non_patient = len("".join(parsed_line[:3]))+2
                self.patients[patient_id] = (stripped_line[non_patient+1:], set()) 
          elif parsed_line[1] == "EXAM":
              if patient_id in self.patients and exam_id not in self.exams:
                # If patient id exists and exam id does not exist, adds an exam
                self.exams[exam_id] = patient_id
                self.patients[patient_id][1].add(exam_id)
        elif parsed_line[0] == "DEL":
            if parsed_line[1] == "PATIENT":
              patient_id = parsed_line[2]
              if patient_id in self.patients:
                for exam in self.patients[patient_id][1]:
                  # Iterate over set of exams and delete them
                  del self.exams[exam]
                del self.patients[patient_id]
            elif parsed_line[1] == "EXAM":
              exam_id = parsed_line[2]
              if exam_id in self.exams:
                corresponding_patient_id = self.exams[exam_id]
                # Remove exam from patient records
                self.patients[corresponding_patient_id][1].remove(exam_id)
                del self.exams[exam_id]
        line = f.readline()
  def output_data(self):
    for id,data in self.patients.items():
      self.ans.append("Name: " + str(data[0]) + ", Id: " + id + ", Exam Count: " + str(len(data[1])))


class Test():
    default_test_ans = ["Name: JOHN DOE, Id: 123, Exam Count: 0", "Name: JANE CROW, Id: 789, Exam Count: 2"]
    adding_edge_cases_ans = ["Name: JOHN JOE, Id: 321, Exam Count: 1", "Name: JANE SMITH, Id: 123, Exam Count: 0"]
    just_deletes_ans = []
    delete_edge_cases_ans = ["Name: JAMES CORDEN, Id: 250, Exam Count: 1"]
    all_functionality_ans = ["Name: JOHN SMITH, Id: 001, Exam Count: 0", "Name: ALEX RIDER, Id: 321, Exam Count: 1", "Name: STEPH CURRY, Id: 030, Exam Count: 2"]
    all_functionality_2_ans = ["Name: ALEX RIDER, Id: 321, Exam Count: 1", "Name: STEPH CURRY, Id: 030, Exam Count: 2"]

    def dataFunction(self,project, input_file):
      project.open_file_and_process_input(input_file)
      project.output_data()
      return project.ans

    def test_default_test(self):
      p = Project()
      unittest.TestCase().assertCountEqual(self.dataFunction(p,"./data/data.txt"),self.default_test_ans)
        
    def test_adding_edge_cases(self):
      p = Project()
      unittest.TestCase().assertCountEqual(self.dataFunction(p,"./data/data2.txt"),self.adding_edge_cases_ans)

    def test_just_deletes(self):
      p = Project()
      unittest.TestCase().assertCountEqual(self.dataFunction(p, "./data/data3.txt"), self.just_deletes_ans)

    def test_deleting_edge_cases(self):
      p = Project()
      unittest.TestCase().assertCountEqual(self.dataFunction(p, "./data/data4.txt"), self.delete_edge_cases_ans) 

    def test_all_functionality(self):
      p = Project()
      unittest.TestCase().assertCountEqual(self.dataFunction(p, "./data/data5.txt"), self.all_functionality_ans)

    def test_all_functionality_2(self):
      p = Project()
      unittest.TestCase().assertCountEqual(self.dataFunction(p, "./data/data6.txt"), self.all_functionality_2_ans)