# -*- coding: utf-8 -*-
#coding=utf-8
import web,time
from action.base import base as baseAction
import model
class testcase(baseAction):
    def __init__(self):
        if self.isLogin() != True:
            raise web.seeother('/')
        baseAction.__init__(self)
        settings = self.getSettings()
        self.assignTplDir(settings.ADMIN_TPL_DIR)
    def save(self):
        userInput = self.getInput()
        date = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        data={
            'CASE_NAME':userInput['casename'],
			'PAGE_URL':userInput['pageurl'],
            'CASE_CONTENT':self.htmlunquote(userInput['content']),
			'FILE_NAME':userInput['filename'],
            'CREATE_TIME':date
        }
        print data
        status = model.testcase().insert(data)
        return self.success('保存成功') if status else self.error('保存失败')
    def add(self):
        print "===add======"
        return self.display('caseAdd')
	