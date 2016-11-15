#!/usr/bin/env python

import lstar, minimally_adequate_teacher

import subprocess

class ABMat(minimally_adequate_teacher.MinimallyAdequateTeacher):
    def isMember(self, inp):
        ret = subprocess.call(["../ab-test/kernel", '"'+inp+'"'])
        if ret == 0:
            return True
        else:
            return False

alphabet = ['a','b']
mat = ABMat()

learner = lstar.LStar(alphabet, mat, verbose=5, seed=0)

print learner.learn()