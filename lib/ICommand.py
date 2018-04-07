"""
 Created by PyCharm Community Edition.
 User: Anton Vasiliev <bysslaev@gmail.com>
 Date: 07/04/2018
 Time: 15:09

"""

from abc import ABCMeta, abstractmethod


class ICommand():
    """
    Абстрактный (на сколько это возможно) класс команды
    """
    __metaclass__ = ABCMeta

    def __init__(self, form):
        """
        :param gui.NotepadForm form:
        """
        self.form = form

    @abstractmethod
    def execute(self):
        """Выполняет комманду"""
