import unittest
import sys
class Project:
  patients = {}
  exams = {}
  ans = []
  def open_file_and_process_input(self, file):
    with open(file, 'r') as f:
      line = f.readline()
      while line:
        stripped_line = line.strip()
        parsed_line = stripped_line.split(" ")        
        if parsed_line[0] == "ADD":
            if parsed_line[1] == "PATIENT":
              if parsed_line[2] not in self.patients:
                non_patient = len("".join(parsed_line[:3]))+2
                self.patients[parsed_line[2]] = (stripped_line[non_patient+1:], set()) 
            elif parsed_line[1] == "EXAM":
              if parsed_line[2] in self.patients and parsed_line[3] not in self.exams:
                self.exams[parsed_line[3]] = parsed_line[2]  
                self.patients[parsed_line[2]][1].add(parsed_line[3])
        elif parsed_line[0] == "DEL":
            if parsed_line[1] == "PATIENT":
              if parsed_line[2] in self.patients:
                for exam in self.patients[parsed_line[2]][1]:
                  # Iterate over set of exams and delete them
                  del self.exams[exam]
                del self.patients[parsed_line[2]]
            elif parsed_line[1] == "EXAM":
              if parsed_line[2] in self.exams:
                corresponding_patient = self.exams[parsed_line]
                # Remove exam from patient records
                self.patients[corresponding_patient][1].remove(parsed_line[2])
                del self.exams[parsed_line[2]]
        line = f.readline()
  def print_output(self):
    for id,data in self.patients.items():
      self.ans.append("Name: " + str(data[0]) + ", Id: " + id + ", Exam Count: " + str(len(data[1])))


class Test():
    p = Project()
    test_1_ans = ['Name: JOHN DOE, Id: 123, Exam Count: 0', 'Name: JANE CROW, Id: 789, Exam Count: 2']
    def dataFunction(self, input_file):
        self.p.open_file_and_process_input(input_file)
        self.p.print_output()
        return self.p.ans
    
    def test_1(self):
        unittest.TestCase().assertCountEqual(self.dataFunction("./data/data.txt"),self.test_1_ans )
