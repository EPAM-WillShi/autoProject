# -*- coding: utf-8 -*-
"""
@author:     Angelia yao
@date:       2018/4/11
"""
import os
import time
import sys
import argparse
import webbrowser
from lib.log import Log


USAGE_STR = '{} [param options]'
DESC_STR = 'This is the description how to run {}'
VERSION_STR = '{} version 1.0'
EXAMPLE_STR = """
example: 
{} -w auto_gui
{} --case xx.py xx.py:case
{} --id [seq]
{} --falied """

class Runner():
    """
    This class driver test cases then run testing.
    """
    def __init__(self):
        pass
    
    def setUp(self):
        """
        SetUp environment
        """
        Log.info('Init the test environment')
        '''
        print information under commandLine
        '''     
        
    def tearDown(self):
        
        '''
        clear up the test environmet
        '''
        Log.info('clear the test environment')
        Log.close()
        
    def get_param(self,output_report):
        
        """
        Define params for programe.
        """        
        programe = os.path.basename(sys.argv[0])
        parser = argparse.ArgumentParser(
        usage=USAGE_STR.format(programe),
        description=DESC_STR.format(programe),
        version=VERSION_STR.format(programe),
        epilog=EXAMPLE_STR.format(*(programe,) * 4),
        formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument('nosetests', action="store_const", const='-v')
        parser.add_argument('-r', '--report', metavar='report_name',
                            action="store", dest='--with-html --html-report',
                            default=output_report,
                            help='generate html report')
        parser.add_argument('-s', action="store_true",
                            dest='-s', default=argparse.SUPPRESS,
                            help='print debug info')
        parser.add_argument('-w', '--where', metavar='case_path', action="store",
                            dest="--where", default=argparse.SUPPRESS,
                            help='the path of case to run')
        parser.add_argument('-c', '--collect', action="store_true",
                            dest='--collect-only', default=argparse.SUPPRESS,
                            help='collect the test case')
        parser.add_argument('--case', nargs='*', metavar='module or case',
                            default=argparse.SUPPRESS, help='case name')
        parser.add_argument('--failed', action="store_true", dest='--failed',
                            default=argparse.SUPPRESS, help='rerun failed case')
        parser.add_argument('--id', metavar='seq', type=int, nargs='*',
                            dest='--with-id', default=argparse.SUPPRESS,
                            help='The sequence of the case')
        args = parser.parse_args()
        params = vars(args)
        return params

        
    def runTest(self): 
        ''' 
        get case then run testing
        '''
        cmd = []
        # set report name
        reportName =  "TestReport.html"
        Log.debug('start : run test method under Runner.py')
        self.setUp()
        version = 'python ' + str(sys.version)
        Log.info(version)
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        output_report = "report/{}_{}".format(now, reportName) 
        params = self.get_param(output_report)   
        for key, value in params.items():
            if key == 'nosetests':
                cmd.insert(0, '{} {}'.format(key, value))
            elif key == 'case':
                cmd.append(' '.join(value))
            elif key == '--with-id':
                cmd.append('{}'.format(key))
                if value:
                    value = [str(i) for i in value]
                    cmd[-1] = cmd[-1] + ' ' + ' '.join(value)
            elif value is True:
                cmd.append('{}'.format(key))
            else:
                cmd.append('{} {}'.format(key, value))
        #cmd.append(" -–with-ignore-docstrings")
        runcmd = ' '.join(cmd)
        print "[INFO]: Running testing under " + version
        print '****************************************'
        print 'Current time is %s' %now  
        print runcmd
        os.system(runcmd)
        Log.info('finish run test cases')
        try:
            reportpath = os.path.abspath(output_report)
            webbrowser.open_new(reportpath)
        except BaseException,Error:
            print 'Error happend when open the test report:' + Error
            
            
if __name__ == '__main__':
    test = Runner().runTest()
