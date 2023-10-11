import datetime
import os


def count_lectures():
    a = os.listdir("lecture-notes")
    count = 0
    for i in a:
        if i.split('.')[0] == 'lecture_notes':
            count += 1
    return count 

def main():
    print( "making lecutre notes for: ", datetime.date.today())
    lecture_number = count_lectures() + 1 

    with open(f"lecture-notes/lecture_notes.{lecture_number}.md", 'w') as f:
        f.writelines(
            f"Lecture {lecture_number}: Quantum many body dynamics \
             \n==================================================== \
             \n#### Date: {datetime.date.today()} \
             \n \
             \nIntro/ Recap: \
             \n------------- \
             \n \
             \nSummary: \
             \n-------- \
             \n \
             \nTodo: \
             \n----- \
             \n \
             \nRef: \
             \n----"
             ) 

  
if __name__ == '__main__':
    main()
