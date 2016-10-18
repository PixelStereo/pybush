#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Project Class is the root class
A project must contains applications
It might contains scenario, which is useful to drive applications
But it might it use only with applications and active mappings between input applications and output applications
"""

import datetime
from pybush import __version__
from pybush.application import Application
#from pybush.scenario import Scenario
from pybush.constants import __dbug__, __projects__

def new_project(name=None):
    """
    Create a new project
    """
    new_proj = Project(name=name)
    __projects__.append(new_proj)
    return new_proj

def projects():
    """
    Return the list of the existing projects
    """
    return __projects__

class Project(Application):
    """
    Project class, will host applications, scenario, mappings etc…
    """
    def __init__(self, **kwargs):
        super(Project, self).__init__(**kwargs)
        self._applications = []
        # from pylekture
        self._lastopened = None
        self._created = str(datetime.datetime.now())
        self._scenario = []
        self._events = []
        self._version = __version__

    def reset(self):
        """reset a project by deleting project.attributes, scenario and events related"""
        # reset project attributes
        self._version = None
        self._path = None
        # reset scenario
        self._scenario = []
        # reset  events
        self._events = []

    def __repr__(self):
        printer = 'Project (name:{name})'
        return printer.format(name=self.name)

    def export(self):
        """
        export Node to a json_string/python_dict with all its properties
        """
        proj = {'applications':[], 'scenario':[]}
        for application in self.applications:
            proj['applications'].append(application.export())
        for scenar in self.scenario:
            proj['scenario'].append(scenar.export())
        return proj

    def new_application(self, dict_import=None, name=None, tags=None, version=None, author=None):
        """
        Create a new application
            :return node object if successful
            :return False if name is not valid (already exists or is not provided)
        """
        if isinstance(dict_import, dict):
            # we import a python dict to create the child
            # be careful about children and parameter
            # which needs to instanciate Classes Node and Parameter
            self.applications = Application(parent=None, name=dict_import['name'], 
                                    version=dict_import['version'], author=dict_import['author'], \
                                    tags=dict_import['tags'])
        else:
            # if the child argument is only a string, this is the name of the new_child to create
            self.applications = Application(name=name, tags=tags, version=version, author=author)
        return self.applications[-1]

    @property
    def applications(self):
        """
        return a list of applications
        """
        return self._applications
    @applications.setter
    def applications(self, the_new_application):
        if self._applications is None:
            self._applications = [the_new_application]
        else:
            self._applications.append(the_new_application)

    def scenario_set(self, old, new):
        """Change order of a scenario in the scenario list of the project"""
        s_temp = self._scenario[old]
        self._scenario.pop(old)
        self._scenario.insert(new, s_temp)

    @property
    def scenario(self):
        """
        Report existing scenario

        :return: All Scenario of this project
        :rtype: list
        """
        return self._scenario

    def new_scenario(self, **kwargs):
        """
        Create a new scenario for this Project
            :args: Optional args are every attributes of the scenario, associated with a keyword
            :rtype: Scenario object
        """
        taille = len(self._scenario)
        scenario = Scenario(parent=self)
        self._scenario.append(scenario)
        for key, value in kwargs.items():
            if key == 'events':
                for event in value:
                    scenario.add_event(self.events[event])
            else:
                setattr(self._scenario[taille], key, value)
        return scenario

    def del_scenario(self, scenario):
        """
        delete a scenario of this project
        This function won't delete events of the scenario
        """
        if scenario in self.scenario:
            # delete the scenario
            self._scenario.remove(scenario)
        else:
            if debug:
                print("ERROR - trying to delete a scenario which not exists \
                      in self._scenario", scenario)

    @property
    def lastopened(self):
        """
        Datetime of the last opened date of this project. Default is None

        :getter: datetime object
        :type getter: string
        """
        return self._lastopened

    @property
    def created(self):
        """
        Datetime of the creation of the project

        :getter: datetime object
        :type getter: string
        """
        return self._created

    def load(self, filepath):
        """
        Fillin Bush with objects created from a json file

        Creates Outputs, Scenario and Events obects
        First, dump attributes, then outputs, scenario and finish with events.

        :returns: True if file formatting is correct, False otherwise
        :rtype: boolean
        """
        # self.read is a method from File Class
        file_content = self.read(filepath)
        # TODO : CHECK IF THIS IS A VALID PROJECT FILE
        # if valid python dict / json file
        if file_content:
            if __dbug__:
                print('loading project called : ' + filepath)
        else:
            if __dbug__:
                print('ERROR 901 - file provided is not a valid file' + str(filepath))
        try:
            for application_dict in file_content['applications']:
                # create a application object for all applications
                if __dbug__:
                    print('------- new-application : ' + application_dict['name'] + ' ------ ')
                application = self.new_application(application_dict['name'])
                # iterate each attributes of the selected application
                for prop, value in application_dict.items():
                    if value:
                        if prop == 'children':
                            # the application has children
                            for child in value:
                                application.new_child(child)
                        elif prop == 'parameter':
                            if __dbug__:
                                print('no parameter for application')
                                #application.make_parameter(value)
                        elif prop == 'outputs':
                            if __dbug__:
                                print('import will create an output')
                                application.new_output(value)
                        else:
                            # register value of the given attribute for the application
                            setattr(application, prop, value)
                if __dbug__:
                    print('application loaded : ' + application.name)
            return True
        # catch error if file is not valid or if file is not a valide node
        except (IOError, ValueError) as error:
            if __dbug__:
                print(error, "ERROR 902 - application cannot be loaded, this is not a valid Application")
            return False
