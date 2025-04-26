import random

class BiochemCareer:
    def __init__(self):
        self.level = 1
        self.performance = 0

        self.levels = {
            1: "Lab Intern",
            2: "Gel Electrophoresis Enthusiast",
            3: "Caffeine-Enhanced Grad Student",
            4: "Chromatography Beginner",
            5: "Postdoc in Purgatory",
            6: "Principal Investigator",
            7: "Biotechnician"
        }

        self.salaries = {
            1: 15,
            2: 22,
            3: 30,
            4: 45,
            5: 55,
            6: 75,
            7: 100
        }

        self.tasks = {
            1: "Micropipette Practice",
            2: "Run a Gel",
            3: "Cry While Analyzing Data",
            4: "Break the Mass Spec",
            5: "Apply for Grant Money",
            6: "Micromanage Lab Students",
            7: "Give Ted Talk About Biotech"
        }

        self.outcomes = [
            ("Successful experiment! Everything worked perfectly.", 10),
            ("Slight contamination... but you covered it up nicely.", 5),
            ("Spilled ethanol everywhere. Lab smells like a frat party.", -2),
            ("Pipetted into wrong wells. You need a coffee.", -3),
            ("Accidentally created fluorescent mold. Kinda cool?", 7),
            ("Knocked over an entire tray of samples. Epic fail.", -8),
            ("Made a breakthrough and got published!", 15),
            ("Forgot to add buffer. Spent 4 hours staring at a broken gel.", -5),
            ("Supervisor stole your idea. Emotional damage.", -6),
            ("Dropped a very expensive beaker. Ran away immediately.", -4),
            ("Saved the day with last-minute troubleshooting!", 12)
        ]

    def go_to_work(self):
        event, performance_change = random.choice(self.outcomes)
        print(f"\n{event}")
        self.performance += performance_change

        self.performance = max(min(self.performance, 30), -10)

        if self.performance >= 20:
            self.promote()
        elif self.performance <= -10:
            self.demote()

    def promote(self):
        if self.level < len(self.levels):
            self.level += 1
            self.performance = 0
            print(f"\nPROMOTION! New Title: {self.levels[self.level]} (Salary: §{self.salaries[self.level]}/hr)")
        else:
            print("\nYou’ve reached the top of the Biochem career!")

    def demote(self):
        if self.level > 1:
            self.level -= 1
            self.performance = 0
            print(f"\nDEMOTION... New Title: {self.levels[self.level]} (Salary: §{self.salaries[self.level]}/hr)")
        else:
            print("\nYou can't be demoted any further... you're already at the bottom!")

    def career_status(self):
        print(f"\nCareer Status:")
        print(f"Level {self.level}: {self.levels[self.level]}")
        print(f"Salary: §{self.salaries[self.level]}/hr")
        print(f"Current Task: {self.tasks[self.level]}")
        print(f"Performance Points: {self.performance}")


my_sim = BiochemCareer()

my_sim.career_status()

for day in range(10):
    print(f"\n--- Day {day+1} ---")
    my_sim.go_to_work()
    my_sim.career_status()









    
