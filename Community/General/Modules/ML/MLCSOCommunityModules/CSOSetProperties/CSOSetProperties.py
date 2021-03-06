#-----------------------------------------------------------------------
#
# Copyright (c) 2010, Biomedical Imaging Group Rotterdam (BIGR), 
# Departments of Radiology and Medical Informatics, Erasmus MC. All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of BIGR nor the names of its contributors 
#       may be used to endorse or promote products derived from this software 
#       without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL BIGR BE LIABLE FOR ANY DIRECT, INDIRECT, 
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT 
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, 
# OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF 
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF 
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#----------------------------------------------------------------------------------
# CSOSetProperties GUI definitions.
#
# \file    CSOSetProperties.script
# \author  Reinhard Hameeteman
# \date    2010-03-02
#
#----------------------------------------------------------------------------------

from mevis import *

def SetEnableState(event = None):
  excludedFields = ['CSOClearSelectionFld','GroupClearSelectionFld']
  filter = ctx.control("filter")
  name = filter.eventControl().getName()
  if name not in excludedFields :
    setName = 'set'+ name[:-3]
    ctx.field( setName ).value = not ctx.field( setName ).boolValue()
  return 


#//# MeVis signature v1
#//# key: MFowDQYJKoZIhvcNAQEBBQADSQAwRgJBALMoAKeDufSkjPLfaCUd7Ij4IgEsndoDH9mP+jpEXKnAczgkSCgtNyNEMyiLur8xV1zEN7f71aeTOVWVntbzpucCARE=:lD+X/cPXp4xBkg/BH8EhyVWLOXzUCvL/ccrRKrYcyKMt2wR4QiXj1OCsqQukghRS1dwd5fRaB39vHgPZUYpdyA==
#//# owner: EMC
#//# date: 2010-03-02T15:15:35
#//# hash: GPCQuNrO38gzKP73viu5TNs71mKHjFdYR5Yxtd2/oHtAUxoL10k8HhEYhjT672GKYYWsOl/rb+Lyqly69S5aLg==
#//# MeVis end
