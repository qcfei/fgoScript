'''
Author: jk 1875809993@qq.com
Date: 2023-03-11 19:30:40
LastEditors: jk 1875809993@qq.com
LastEditTime: 2023-03-11 20:48:28
FilePath: \decline\miniInstall.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import re
import subprocess


def minitouch_install(minitouch_fn:str):
    cmd('adb push  {} /data/local/tmp'.format(minitouch_fn))
    cmd('adb shell chmod 777 /data/local/tmp/minitouch')


def minicap_install(minicapso_fn:str,minicap_fn:str):
    cmd('adb push  {} /data/local/tmp'.format(minicap_fn))
    cmd('adb push  {} /data/local/tmp'.format(minicapso_fn))
    cmd('adb shell chmod 777 /data/local/tmp/minicap')


def mnq_para_get():
    struc=subprocess.getoutput('adb shell getprop ro.product.cpu.abi')
    sdk=subprocess.getoutput('adb shell getprop ro.build.version.sdk')

    return struc,sdk


def cmd(text:str):
    txt=text.replace('adb',r'platform-tools_r33.0.3-windows\platform-tools\adb.exe')
    subprocess.run(txt, shell=True)


def install(ip:str):
    cmd('adb connect {}'.format(ip))
    struc,sdk=mnq_para_get()
    minicapso_fn=r'minicap\minicap-shared\aosp\libs\android-{}\{}\minicap.so'.format(sdk,struc)
    minicap_fn=r'minicap\{}\minicap'.format(struc)
    minitouch_fn=r'minitouch\{}\minitouch'.format(struc)
    mnq_fs_str=subprocess.getoutput('adb shell ls /data/local/tmp')

    if not re.findall('minitouch',mnq_fs_str):
        minitouch_install(minitouch_fn)
    else:
        cmd('adb shell rm -r /data/local/tmp/minitouch')
        minitouch_install(minitouch_fn)
    if not re.findall('minitouch',mnq_fs_str):
        minicap_install(minicapso_fn,minicap_fn)
    else:
        cmd('adb shell rm -r /data/local/tmp/minicap')
        cmd('adb shell rm -r /data/local/tmp/minicap.so')
        minicap_install(minicapso_fn,minicap_fn)
    cmd('adb disconnect')

    return True


if __name__ == '__main__':

    cmd('adb connect 127.0.0.1:62001')
    struc,sdk=mnq_para_get()
    minicapso_fn=r'minicap\minicap-shared\aosp\libs\android-{}\{}\minicap.so'.format(sdk,struc)
    minicap_fn=r'minicap\{}\minicap'.format(struc)
    minitouch_fn=r'minitouch\{}\minitouch'.format(struc)
    mnq_fs_str=subprocess.getoutput('adb shell ls /data/local/tmp')

    if not re.findall('minitouch',mnq_fs_str):
        minitouch_install(minitouch_fn)
    else:
        cmd('adb shell rm -r /data/local/tmp/minitouch')
        minitouch_install(minitouch_fn)
    if not re.findall('minitouch',mnq_fs_str):
        minicap_install(minicapso_fn,minicap_fn)
    else:
        cmd('adb shell rm -r /data/local/tmp/minicap')
        cmd('adb shell rm -r /data/local/tmp/minicap.so')
        minicap_install(minicapso_fn,minicap_fn)


    b=0
