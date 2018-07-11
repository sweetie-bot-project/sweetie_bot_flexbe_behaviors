#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from flexbe_states.operator_decision_state import OperatorDecisionState
from sweetie_bot_flexbe_states.set_bool_state import SetBoolState
from sweetie_bot_flexbe_states.text_command_state import TextCommandState
from sweetie_bot_flexbe_states.rand_head_movements_state import SweetieRandHeadMovementsState
from sweetie_bot_flexbe_states.animation_stored_trajectory_state import AnimationStoredJointTrajectoryState
from flexbe_states.decision_state import DecisionState
from flexbe_manipulation_states.srdf_state_to_moveit import SrdfStateToMoveit
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

import random

# [/MANUAL_IMPORT]


'''
Created on Sun Mar 19 2017
@author: disrecord
'''
class sweetie_bot_flexbe_testSM(Behavior):
	'''
	Test behavior for AnimationStoredJointTrajectoryState, TextCommandState, SetBoolState
	'''


	def __init__(self):
		super(sweetie_bot_flexbe_testSM, self).__init__()
		self.name = 'sweetie_bot_flexbe_test'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:583 y:683, x:578 y:422
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.unused = None

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:278 y:24
			OperatableStateMachine.add('SesectBehavior',
										OperatorDecisionState(outcomes=['dance', 'rand_moves'], hint='Select behavior', suggestion='dance'),
										transitions={'dance': 'TestMovement', 'rand_moves': 'TurnOnJointStateController'},
										autonomy={'dance': Autonomy.Full, 'rand_moves': Autonomy.Full})

			# x:114 y:352
			OperatableStateMachine.add('TurnOffJointStateController',
										SetBoolState(service='motion/controller/joint_state/set_operational', value=False),
										transitions={'true': 'SingASong', 'false': 'failed', 'failure': 'failed'},
										autonomy={'true': Autonomy.High, 'false': Autonomy.Off, 'failure': Autonomy.Off},
										remapping={'success': 'success', 'message': 'message'})

			# x:136 y:518
			OperatableStateMachine.add('SingASong',
										TextCommandState(type='voice/play_wav', command='mmm_song', topic='control'),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Full})

			# x:882 y:207
			OperatableStateMachine.add('RandEyes',
										SweetieRandHeadMovementsState(topic='motion/controller/joint_state/out_joints_src_reset', duration=20, interval=[2,3], max2356=[ 0.5, 0.5, 1.5, 1.5], min2356=[-0.5,-0.5,-1.5,-1.5]),
										transitions={'done': 'RandSelector'},
										autonomy={'done': Autonomy.Off})

			# x:248 y:213
			OperatableStateMachine.add('TestMovement',
										AnimationStoredJointTrajectoryState(action_topic='motion/controller/joint_trajectory', trajectory_param='joint_trajectory/dance14'),
										transitions={'success': 'TurnOffJointStateController', 'partial_movement': 'failed', 'invalid_pose': 'failed', 'failure': 'failed'},
										autonomy={'success': Autonomy.Low, 'partial_movement': Autonomy.Off, 'invalid_pose': Autonomy.Off, 'failure': Autonomy.Off},
										remapping={'result': 'result'})

			# x:591 y:109
			OperatableStateMachine.add('TurnOnJointStateController',
										SetBoolState(service='motion/controller/joint_state/set_operational', value=True),
										transitions={'true': 'RandEyes', 'false': 'RandEyes', 'failure': 'failed'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off, 'failure': Autonomy.Off},
										remapping={'success': 'success', 'message': 'message'})

			# x:939 y:351
			OperatableStateMachine.add('RandSelector',
										DecisionState(outcomes=['first','second'], conditions=(lambda x: 'first' if random.uniform(0,1) < 0.5 else 'second')),
										transitions={'first': 'PlaceHead', 'second': 'TestMovement'},
										autonomy={'first': Autonomy.Full, 'second': Autonomy.Full},
										remapping={'input_value': 'unused'})

			# x:704 y:603
			OperatableStateMachine.add('HeadShake',
										AnimationStoredJointTrajectoryState(action_topic='motion/controller/joint_trajectory', trajectory_param='joint_trajectory/head_shake'),
										transitions={'success': 'finished', 'partial_movement': 'failed', 'invalid_pose': 'failed', 'failure': 'failed'},
										autonomy={'success': Autonomy.Off, 'partial_movement': Autonomy.Off, 'invalid_pose': Autonomy.Off, 'failure': Autonomy.Off},
										remapping={'result': 'result'})

			# x:958 y:510
			OperatableStateMachine.add('PlaceHead',
										SrdfStateToMoveit(config_name='head_basic', move_group='head', action_topic='move_group', robot_name=''),
										transitions={'reached': 'HeadShake', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
