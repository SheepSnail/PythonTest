#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def valid_password(pwd):
    if pwd[0].isalpha():
        if pwd[-1].isalpha() or pwd[-1].isdigit():
            if len(pwd) >= 2 and len(pwd) <= 10:
                for x in pwd:
                    if x.isalpha() or x.isdigit() or x == '_':
                        pass
                    else:
                        return False
                return True
    return False
pwd = input('password:')
print(valid_password(pwd))
