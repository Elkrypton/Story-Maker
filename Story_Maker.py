from tkinter import *

class Application(Frame):

    def __init__(self,master):

        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        Label(self,
            text="Enter the information for a new story").grid(row=0,
            column=1,sticky=W)
        Label(self,
            text="Person:",font="comicsansms").grid(row=1,column=0,sticky=W)

        self.person = Entry(self,bg="grey",fg="blue",font="comicsansms",bd=10)
        self.person.grid(row=1,column=1,padx=2,pady=2,sticky=W)

        Label(self,
            text = "Plural Noun:",font="comicsansms").grid(row=2,column=0,sticky=W)
        self.plural = Entry(self, font="comicsansms",bg="grey",bd=10,fg="blue")
        self.plural.grid(row=2,padx=2,pady=2,column=1,sticky=W)

        Label(self,
            text="verb:",font="comicsansms").grid(row=3,column=0,sticky=W)

        self.verb = Entry(self,font="comicsansms",fg="blue",bg="grey",bd=10)

        self.verb.grid(row=3,column=1,padx=2,pady=2,sticky=W)

        Label(self,font="comicsansms",
            text="Adjective:").grid(row=4,column=0,sticky=W)

        self.itchy = BooleanVar()

        Checkbutton(self,
            text="Itchy",
            variable = self.itchy).grid(row=4,
            column = 1,sticky=W)

        self.joy = BooleanVar()
        Checkbutton(self,
            text="Joyous",font="comicsansms",
            variable = self.joy).grid(row=4,
            column=2,sticky=W)

        self.electric = BooleanVar()
        Checkbutton(self,
            text="Electric",font="comicsansms",
            variable = self.electric).grid(row=4,
            column=3,sticky=W)


        Label(self,font="comicsansms",
            text='Body Part:').grid(row=5,column=0,sticky=W)

        self.body_part = StringVar()
        self.body_part.set(None)
        body_parts = ["bellybutton","big toe","eyes"]
        column = 1

        for part in body_parts:

            Radiobutton(self,font="comicsansms",
                text = part,
                variable = self.body_part,
                value = part).grid(row=5,column=column,sticky=W)

            column += 1

        Button(self,
            text="Click For story",font="comicsansms",bg="grey",
            command = self.tell_story).grid(row=6,column=0,sticky=W)

        self.story_text = Text(self,bd=25,font="comicsansms",bg="black",fg="green",
            spacing1 = 1,
            spacing2 = 1,
            spacing3 = 1,

            #selectborderwidth = 4
            width=75,
            height = 10,
            wrap = WORD)
        self.story_text.grid(row=7,column=0,columnspan=4)

    def tell_story(self):

        Person = self.person.get()
        noun = self.plural.get()
        Verb = self.verb.get()
        adjectives = ""

        if self.itchy.get():
            adjectives += "itchy"

        elif self.joy.get():
            adjectives += "joyous"

        elif self.electric.get():
            adjectives += "Electrc"

        body_part = self.body_part.get()
        story = " The famous explorer "
        story += Person
        story += " had nearly given up a life-long quest to find The Lost City of "
        story += noun.title()
        story += " when one day, the  "
        story += noun
        story += " found "
        story += Person + "."
        story += " A strong, "
        story += adjectives
        story += " peculiar feeling overhelmed the explorer. "
        story += " After all this time, the quest was finally over.A tear came to "
        story += Person + "'s "
        story += body_part + ". "
        story += "And then, the "
        story += noun
        
        story += " promptly devoured "
        story += Person + "."
        story += " The moral of the story? Be carful what you "
        story +=  Verb
        story += " for."
        #story += noun 
        


        self.story_text.delete(0.0,END)
        self.story_text.insert(0.0,story)


root = Tk()
app = Application(root)
root.title("Story originator")
root.mainloop()
