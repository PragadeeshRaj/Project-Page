#Data "setup" for Projects 
#next step would be to extract project data from a database
def setup():
  #Person Data
  name = "P2-Einsteins"
  github = "https://github.com/PragadeeshRaj/Raj-Academy"
  Journal1 = "https://docs.google.com/document/d/1BR_-NL6OLtSCz8bhTDnt8godFyw9MgyHKEk1I2nx174/edit?usp=sharing"
  Journal2 = "https://docs.google.com/document/d/18v-SvlNMZ4gJS6WdWzy4DUILUiVfrN0_a1so8DVnq90/edit"
  source = {"name": name, "github": github, "Journal1": Journal1, "Journal2": Journal2}
  #Project Data
  project1 =  "Python Fundamentals"
  projlinks1 = [
    Link("Resources", "https://docs.google.com/document/d/1xPvTYXyzO0jsr4B-iy9nA8Yu-baAbQeymXPf33ssAPI/edit?usp=sharing"),
    Link("Repl Repository", "https://repl.it/@AZPragTeam/ThisIsItBois"),
    Link("Project Plan", "https://padlet.com/pragadeesh3000/8d4vpki73p0z4eac")
  ]
  project2 =  "Calculator"
  projlinks2 = [
    Link("Resources", "https://docs.google.com/document/d/14RrAmqkMqANxfpfV2X1U6TVJ1xknYqJ0yg0QgrA3go8/edit?usp=sharing"),
    Link("Github Repository", "https://github.com/PragadeeshRaj/Raj-Academy"),
    Link("Project Plan", "https://padlet.com/pragadeesh3000/zg8kksq513p2dpsl")
  ]
  #Project Objects
  proj1 = Project(project1, projlinks1)
  proj2 = Project(project2, projlinks2)
  #HTML Data
  projects = Projects(source, [proj1, proj2])
  return projects

#Link class contains button (label) and hypertext reference (href)
class Link():
  #link data with button and href (url)
  def __init__(self, btn, href):
    self.btn = btn
    self.href = href
  def get_btn(self):
    return self.btn
  def get_href(self):
    return self.href

#Project data class contain project name and links (Link class objects)
class Project():
  #project data with name and links
  def __init__(self, name, links):
    self.name = name
    self.links = links
  def get_name(self):
    return self.name
  def get_links(self):
    return self.links

#Projects class contains person (owner) and multiple projects (Project class objects)
class Projects():
  #HTML data with source and projects    
  def __init__(self, source, projects):
    self.source = source
    self.projects = projects
  #source data getter
  def get_source(self):
    return self.source
  #project data getter
  def get_projects(self):
    return self.projects
