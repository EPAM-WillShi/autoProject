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
import platform
from lib.log import Log


USAGE_STR = '{} [param options]'
DESC_STR = 'This is the description how to run {}'
VERSION_STR = '{} version 1.0'
EXAMPLE_STR = """
example: 
{} -w auto_gui
{} --case xx.py xx.py:case
{} --id [seq]
{} --failed """


class Runner:
    """
    This class driver test cases then run testing.
    """
    def __init__(self):
        pass
    
    def setup(self):
        """
        SetUp environment
        """
        Log.info('Init the test environment')
        
    def teardown(self):
        """
        clear up the test environment
        """
        Log.info('clear the test environment')
        Log.close()

    def get_param(self, output_report):
        
        """
        Define params for program.
        """        
        program = os.path.basename(sys.argv[0])
        parser = argparse.ArgumentParser(
            usage=USAGE_STR.format(program),
            description=DESC_STR.format(program),
            version=VERSION_STR.format(program),
            epilog=EXAMPLE_STR.format(*(program,) * 4),
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

    def run_test(self):
        """
        get case then run testing
        """
        cmd = []
        # set report name
        report_name = "TestReport.html"
        Log.debug('start : run test method under Runner.py')
        self.setup()
        version = 'python ' + str(sys.version)
        Log.info(version)
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        output_report = "report/{}_{}".format(now, report_name)
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
        # cmd.append(" -–with-ignore-docstrings")
        runcmd = ' '.join(cmd)
        print "[INFO]: Running testing under " + version
        print '****************************************'
        print 'Current time is %s' % now
        print runcmd
        os.system(runcmd)
        Log.info('finish run test cases')
        try:
            report_path = os.path.abspath(output_report)
            webbrowser.open_new(report_path)
        except BaseException, e:
            Log.error('Error happened when open the test report: %s' % e)
        platform_type = platform.system()
        if platform_type == 'Linux':
            os.system('pkill -9 chrome')
            os.system('pkill -9 firefox')
            os.system('pkill -9 geckodriver')
            print "chrome, firefox and geckodriver processes don't exist."
        elif platform_type == 'Windows':
            os.system('taskkill /F /IM geckodriver.exe')
            os.system('taskkill /F /IM firefox.exe')
            os.system('taskkill /F /IM chrome.exe')
            print "chrome, firefox and geckodriver processes don't exist."
        else:
            print "Currently not support this platform {}".format(platform_type)

            
if __name__ == '__main__':
    test = Runner()
    test.run_test()
