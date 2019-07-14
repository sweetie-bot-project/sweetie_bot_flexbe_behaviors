#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from sweetie_bot_flexbe_states.set_cartesian_pose import SetCartesianPose
from sweetie_bot_flexbe_states.compound_action import CompoundAction
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Sun Jul 14 2019
@author: mutronics
'''
class AutonomousBehaviorSM(Behavior):
	'''
	Autonomous behavior
	'''


	def __init__(self):
		super(AutonomousBehaviorSM, self).__init__()
		self.name = 'AutonomousBehavior'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:459, x:384 y:337
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:89 y:26
			OperatableStateMachine.add('WalkPose',
										SetCartesianPose(controller='motion/controller/stance', pose=[0.0,0.0,0.209,0.0,0.0,0.0], frame_id='base_link_path', frame_is_moving=False, resources=['leg1','leg2','leg3','leg4'], actuator_frame_id='base_link', tolerance_lin=0.001, tolerance_ang=0.0085, timeout=10.0),
										transitions={'done': 'Fwd_Left_Say1', 'failed': 'failed', 'timeout': 'failed'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off, 'timeout': Autonomy.Off})

			# x:88 y:93
			OperatableStateMachine.add('Fwd_Left_Say1',
										CompoundAction(t1=[0,0.0], type1='motion/step_sequence', cmd1='walk_fwd_20', t2=[1,0.0], type2='motion/step_sequence', cmd2='turn_left_20_20_45', t3=[2,0.0], type3='voice/play_wav', cmd3='why_do_i_see_these_creatures', t4=[0,0.0], type4=None, cmd4=''),
										transitions={'success': 'ZeroPose', 'invalid_pose': 'failed', 'failure': 'failed'},
										autonomy={'success': Autonomy.Off, 'invalid_pose': Autonomy.Off, 'failure': Autonomy.Off})

			# x:90 y:161
			OperatableStateMachine.add('ZeroPose',
										SetCartesianPose(controller='motion/controller/stance', pose=[0.0,0.0,0.233,0.0,0.0,0.0], frame_id='base_link_path', frame_is_moving=False, resources=['leg1','leg2','leg3','leg4'], actuator_frame_id='base_link', tolerance_lin=0.001, tolerance_ang=0.0085, timeout=10.0),
										transitions={'done': 'WalkPose', 'failed': 'failed', 'timeout': 'failed'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off, 'timeout': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]