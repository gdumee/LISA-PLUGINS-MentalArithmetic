# -*- coding: UTF-8 -*-
if __name__ != "__main__":
    from lisa.server.plugins.IPlugin import IPlugin
import gettext
import inspect
import json,os

if __name__ == "__main__":
    class IPlugin():
        def __Init():
            pass

class MentalArithmetic(IPlugin):
    """
    Lisa plugin to do mental arithmetics
    """
    def __init__(self):
        super(MentalArithmetic, self).__init__()
        self.configuration_plugin = self.mongo.lisa.plugins.find_one({"name": "MentalArithmetic"})
        self.path = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0], os.path.normpath("../lang/"))))
        self._ = translation = gettext.translation(domain='mentalarithmetic',
                                                   localedir=self.path,
                                                   fallback=True,
                                                   languages=[self.configuration_lisa['lang']]).ugettext

    def addition(self, jsonInput):
        # If json has no wit return (???) or wit didn't understand math expression
        if jsonInput.has_key('outcome') == False or jsonInput['outcome'].has_key('entities') == False or jsonInput['outcome']['entities'].has_key("math_expression") == False:
            return {"plugin": "MentalArithmetic",
                    "method": "addition",
                    "body": self._('Input error')
            }
        math_exp = jsonInput['outcome']['entities']['math_expression']
        
        print math_exp
        
        return {"plugin": "MentalArithmetic",
                "method": "addition",
                "body": self._('Too hard')
        }
