--代理IP表
CREATE TABLE proxyip
(
  ipId               integer PRIMARY KEY AUTOINCREMENT,
  address            text NOT NULL,
  ipName             text,
  zoneName           char(100),
  remark             text
);

--代理服务器表
create table proxyserver
(
  serverId             integer PRIMARY KEY AUTOINCREMENT,
  serverUrl            text NOT NULL,
  paths                text,
  remark               text
);

--代理参数表
create table systemparameter
(
  parameterId      integer PRIMARY KEY AUTOINCREMENT,
  parameterName    text,
  parameterValue   text,
  validateRule     text
);

--系统任务表
create table systemtask
(
  taskId           integer PRIMARY KEY AUTOINCREMENT,
  taskName         char(100),
  siteIds          text,
  taskParams       text,
  sqlTemplate      text,
  dataNumber       integer,
  taskType         integer,
  beginTime        char(20),
  endTime          char(20)
);
