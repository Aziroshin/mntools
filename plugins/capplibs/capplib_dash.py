#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#=======================================================================================
# Imports
#=======================================================================================

from plugins.capplibs.capplib_bitcoin import *

#=======================================================================================
# Library
#=======================================================================================

#==========================================================
class DashCapp(BitcoinCapp):
	
	#=============================
	"""Represents a Dash capp."""
	#=============================
	
	def deleteBlockchainData(self):
		self.deleteDataFiles["blocks", "chainstate", "database", "mncache.dat", "peers.dat", "mnpayments.dat", "banlist.dat"]