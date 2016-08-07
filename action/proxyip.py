# -*- coding: utf-8 -*-
#coding=utf-8
import web,time
from action.base import base as baseAction
import model
class proxyip(baseAction):
    def __init__(self):
        if self.isLogin() != True:
            raise web.seeother('/')
        baseAction.__init__(self)
        settings = self.getSettings()
        self.assignTplDir(settings.ADMIN_TPL_DIR)
    def save(self):
        userInput= self.getInput()
        data={
            'address':userInput['address'],
            'ipName':userInput['ipName'],
            'zoneName':userInput['zoneName'],
            'remark':userInput['remark']
        }
        status = model.proxyip().insert(data)
        if status:
            return self.success('保存成功',self.makeUrl('proxyip','list'))
        else:
            return self.error('保存失败')
    def list(self):
        inputParams = self.getInput()
        page = int(inputParams['page']) if inputParams.has_key('page') else 1
        settings = self.getSettings()
        count = settings.PER_PAGE_COUNT
        offset= (page-1)*count if page > 0 else 0
        proxyIpObj = model.proxyip()
        condition = {}
        listData = proxyIpObj.getOne('COUNT(*) AS `total`',condition)
        totalCount = listData['total']
        proxyIpList = proxyIpObj.getList('*',condition,'ipId desc',str(offset)+','+str(count))
        self.assign('proxyIpList',proxyIpList)
        pageString = self.getPageStr(self.makeUrl('proxyip','list'),page,count,totalCount)
        self.assign('pageString',pageString)
        return self.display('proxyIpList')
    def delete(self):
        inputParams = self.getInput()
        if not inputParams.has_key('id') :
            return self.error('数据不存在')
        id=inputParams['id']
        condition={'id':str(id)}
        result=model.cms().delete(condition)
        if result:
            return self.success('删除成功',self.makeUrl('proxyip','list'))
        else:
            return self.error('删除失败')