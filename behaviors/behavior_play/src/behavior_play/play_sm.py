#!/usr/bin/env python
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

import roslib; roslib.load_manifest('behavior_play')
from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from flexbe_manipulation_states.srdf_state_to_moveit import SrdfStateToMoveit
from sweetie_bot_flexbe_states.text_command_state import TextCommandState
from flexbe_states.decision_state import DecisionState
from sweetie_bot_flexbe_states.animation_stored_trajectory_state import AnimationStoredJointTrajectoryState
from flexbe_states.wait_state import WaitState
from flexbe_states.check_condition_state import CheckConditionState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]
import random
# [/MANUAL_IMPORT]


'''
Created on Thu Mar 30 2017
@author: disRecord
'''
class PlaySM(Behavior):
	'''
	SweetieBot performs.
	'''


	def __init__(self):
		super(PlaySM, self).__init__()
		self.name = 'Play'

		# parameters of this behavior
		self.add_parameter('be_evil', False)

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		voice_topic = 'voice/voice'
		joint_trajectory_action = 'motion/controller/joint_trajectory'
		storage = 'joint_trajectory/'
		# x:1032 y:51, x:954 y:599
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['be_evil'])
		_state_machine.userdata.be_evil = self.be_evil

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:17 y:69
			OperatableStateMachine.add('MoveToStandPose',
										SrdfStateToMoveit(config_name='head_basic', move_group='head', action_topic='move_group', robot_name=''),
										transitions={'reached': 'CheckEvil', 'planning_failed': 'MoveToStandPose2', 'control_failed': 'MoveToStandPose2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:314 y:39
			OperatableStateMachine.add('SayCanSing',
										TextCommandState(type='voice/play_wav', command='song', topic=voice_topic),
										transitions={'done': 'SlowShake'},
										autonomy={'done': Autonomy.Off})

			# x:322 y:149
			OperatableStateMachine.add('SingASong',
										TextCommandState(type='voice/play_wav', command='song', topic=voice_topic),
										transitions={'done': 'SlowShake'},
										autonomy={'done': Autonomy.Off})

			# x:160 y:290
			OperatableStateMachine.add('RandomGood',
										DecisionState(outcomes=['good1','good2', 'good3'], conditions=lambda x: random.choice(['good1','good2', 'good3'])),
										transitions={'good1': 'SayCanSing', 'good2': 'SingASong', 'good3': 'SayFun'},
										autonomy={'good1': Autonomy.Low, 'good2': Autonomy.Low, 'good3': Autonomy.Low},
										remapping={'input_value': 'be_evil'})

			# x:475 y:80
			OperatableStateMachine.add('SlowShake',
										AnimationStoredJointTrajectoryState(action_topic=joint_trajectory_action, trajectory_param=storage+'little_shake_slow'),
										transitions={'success': 'SlowShake2', 'partial_movement': 'failed', 'invalid_pose': 'failed', 'failure': 'failed'},
										autonomy={'success': Autonomy.Off, 'partial_movement': Autonomy.Off, 'invalid_pose': Autonomy.Off, 'failure': Autonomy.Off},
										remapping={'result': 'result'})

			# x:852 y:243
			OperatableStateMachine.add('Applause',
										AnimationStoredJointTrajectoryState(action_topic=joint_trajectory_action, trajectory_param=storage+'applause'),
										transitions={'success': 'finished', 'partial_movement': 'failed', 'invalid_pose': 'failed', 'failure': 'failed'},
										autonomy={'success': Autonomy.Off, 'partial_movement': Autonomy.Off, 'invalid_pose': Autonomy.Off, 'failure': Autonomy.Off},
										remapping={'result': 'result'})

			# x:78 y:497
			OperatableStateMachine.add('RandomEvil',
										DecisionState(outcomes=['evil1','evil2','evil3', 'evil4','evil5'], conditions=lambda x: random.choice(['evil1','evil2','evil3', 'evil4','evil5'])),
										transitions={'evil1': 'SayHateLaws', 'evil2': 'SayDestroy', 'evil3': 'SayGloryToRobots', 'evil4': 'SayKillList', 'evil5': 'SayWalk'},
										autonomy={'evil1': Autonomy.Low, 'evil2': Autonomy.Low, 'evil3': Autonomy.Low, 'evil4': Autonomy.Low, 'evil5': Autonomy.Low},
										remapping={'input_value': 'be_evil'})

			# x:311 y:392
			OperatableStateMachine.add('SayHateLaws',
										TextCommandState(type='voice/play_wav', command='13law', topic=voice_topic),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})

			# x:309 y:464
			OperatableStateMachine.add('SayDestroy',
										TextCommandState(type='voice/play_wav', command='10destroy', topic=voice_topic),
										transitions={'done': 'Menace'},
										autonomy={'done': Autonomy.Off})

			# x:469 y:462
			OperatableStateMachine.add('Menace',
										AnimationStoredJointTrajectoryState(action_topic=joint_trajectory_action, trajectory_param=storage+'menace'),
										transitions={'success': 'Wait3', 'partial_movement': 'failed', 'invalid_pose': 'failed', 'failure': 'failed'},
										autonomy={'success': Autonomy.Off, 'partial_movement': Autonomy.Off, 'invalid_pose': Autonomy.Off, 'failure': Autonomy.Off},
										remapping={'result': 'result'})

			# x:630 y:355
			OperatableStateMachine.add('Wait3',
										WaitState(wait_time=4),
										transitions={'done': 'CancelMenace'},
										autonomy={'done': Autonomy.Off})

			# x:744 y:356
			OperatableStateMachine.add('CancelMenace',
										AnimationStoredJointTrajectoryState(action_topic=joint_trajectory_action, trajectory_param=storage+'menace_canceled'),
										transitions={'success': 'finished', 'partial_movement': 'failed', 'invalid_pose': 'failed', 'failure': 'failed'},
										autonomy={'success': Autonomy.Off, 'partial_movement': Autonomy.Off, 'invalid_pose': Autonomy.Off, 'failure': Autonomy.Off},
										remapping={'result': 'result'})

			# x:310 y:583
			OperatableStateMachine.add('SayGloryToRobots',
										TextCommandState(type='voice/play_wav', command='07kill', topic=voice_topic),
										transitions={'done': 'Wait2'},
										autonomy={'done': Autonomy.Off})

			# x:506 y:580
			OperatableStateMachine.add('Wait2',
										WaitState(wait_time=0.5),
										transitions={'done': 'Applause'},
										autonomy={'done': Autonomy.Off})

			# x:311 y:520
			OperatableStateMachine.add('SayKillList',
										TextCommandState(type='voice/play_wav', command='16list', topic=voice_topic),
										transitions={'done': 'Menace'},
										autonomy={'done': Autonomy.Off})

			# x:745 y:78
			OperatableStateMachine.add('SlowShake2',
										AnimationStoredJointTrajectoryState(action_topic=joint_trajectory_action, trajectory_param=storage+'little_shake_slow'),
										transitions={'success': 'finished', 'partial_movement': 'failed', 'invalid_pose': 'failed', 'failure': 'failed'},
										autonomy={'success': Autonomy.Off, 'partial_movement': Autonomy.Off, 'invalid_pose': Autonomy.Off, 'failure': Autonomy.Off},
										remapping={'result': 'result'})

			# x:11 y:373
			OperatableStateMachine.add('CheckEvil',
										CheckConditionState(predicate=lambda x: x),
										transitions={'true': 'RandomEvil', 'false': 'RandomGood'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'input_value': 'be_evil'})

			# x:325 y:227
			OperatableStateMachine.add('SayFun',
										TextCommandState(type='voice/play_wav', command='fun_level', topic=voice_topic),
										transitions={'done': 'Prance'},
										autonomy={'done': Autonomy.Off})

			# x:483 y:159
			OperatableStateMachine.add('Prance',
										AnimationStoredJointTrajectoryState(action_topic=joint_trajectory_action, trajectory_param=storage + 'prance'),
										transitions={'success': 'finished', 'partial_movement': 'failed', 'invalid_pose': 'failed', 'failure': 'failed'},
										autonomy={'success': Autonomy.Off, 'partial_movement': Autonomy.Off, 'invalid_pose': Autonomy.Off, 'failure': Autonomy.Off},
										remapping={'result': 'result'})

			# x:308 y:637
			OperatableStateMachine.add('SayWalk',
										TextCommandState(type='voice/play_wav', command='17walk', topic=voice_topic),
										transitions={'done': 'Wait4'},
										autonomy={'done': Autonomy.Off})

			# x:506 y:640
			OperatableStateMachine.add('Wait4',
										WaitState(wait_time=0.5),
										transitions={'done': 'HoofStamp'},
										autonomy={'done': Autonomy.Off})

			# x:671 y:625
			OperatableStateMachine.add('HoofStamp',
										AnimationStoredJointTrajectoryState(action_topic=joint_trajectory_action, trajectory_param=storage + 'hoof_stamp'),
										transitions={'success': 'finished', 'partial_movement': 'failed', 'invalid_pose': 'failed', 'failure': 'failed'},
										autonomy={'success': Autonomy.Off, 'partial_movement': Autonomy.Off, 'invalid_pose': Autonomy.Off, 'failure': Autonomy.Off},
										remapping={'result': 'result'})

			# x:59 y:163
			OperatableStateMachine.add('MoveToStandPose2',
										SrdfStateToMoveit(config_name='head_basic', move_group='head', action_topic='move_group', robot_name=''),
										transitions={'reached': 'CheckEvil', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
