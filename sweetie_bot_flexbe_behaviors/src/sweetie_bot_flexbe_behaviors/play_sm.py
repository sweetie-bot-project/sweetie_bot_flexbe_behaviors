#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from flexbe_manipulation_states.srdf_state_to_moveit import SrdfStateToMoveit
from sweetie_bot_flexbe_states.text_command_state import TextCommandState
from flexbe_states.decision_state import DecisionState
from sweetie_bot_flexbe_states.execute_stored_trajectory_state import ExecuteStoredJointTrajectoryState
from flexbe_states.wait_state import WaitState
from flexbe_states.check_condition_state import CheckConditionState
from sweetie_bot_flexbe_states.sweetie_bot_compound_action_state import SweetieBotCompoundAction
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
		voice_topic = 'control'
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
										SrdfStateToMoveit(config_name='head_upright', move_group='head', action_topic='move_group', robot_name=''),
										transitions={'reached': 'CheckEvil', 'planning_failed': 'MoveToStandPose2', 'control_failed': 'MoveToStandPose2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:314 y:2
			OperatableStateMachine.add('SingSong1',
										TextCommandState(type='voice/play_wav', command='beep_beep_im_a_sheep', topic=voice_topic),
										transitions={'done': 'SlowShake'},
										autonomy={'done': Autonomy.Off})

			# x:313 y:73
			OperatableStateMachine.add('SingSong2',
										TextCommandState(type='voice/play_wav', command='bot_im_a_sweetie_bot_and_i_dance', topic=voice_topic),
										transitions={'done': 'SlowShake'},
										autonomy={'done': Autonomy.Off})

			# x:160 y:290
			OperatableStateMachine.add('RandomGood',
										DecisionState(outcomes=['good1','good2', 'good3', 'good4', 'good5', 'good6'], conditions=lambda x: random.choice(['good1','good2', 'good3', 'good4', 'good5', 'good6'])),
										transitions={'good1': 'SingSong1', 'good2': 'SingSong2', 'good3': 'SaySweetieInfantery', 'good4': 'SayCuiteMark', 'good5': 'SayHumansEverywhere', 'good6': 'SingDance'},
										autonomy={'good1': Autonomy.Low, 'good2': Autonomy.Low, 'good3': Autonomy.Low, 'good4': Autonomy.Low, 'good5': Autonomy.Low, 'good6': Autonomy.Low},
										remapping={'input_value': 'be_evil'})

			# x:498 y:26
			OperatableStateMachine.add('SlowShake',
										ExecuteStoredJointTrajectoryState(action_topic=joint_trajectory_action, trajectory_param=storage+'little_shake_fast'),
										transitions={'success': 'finished', 'partial_movement': 'failed', 'invalid_pose': 'failed', 'failure': 'failed'},
										autonomy={'success': Autonomy.Off, 'partial_movement': Autonomy.Off, 'invalid_pose': Autonomy.Off, 'failure': Autonomy.Off},
										remapping={'result': 'result'})

			# x:669 y:556
			OperatableStateMachine.add('PointOnSomethingEvil',
										ExecuteStoredJointTrajectoryState(action_topic=joint_trajectory_action, trajectory_param=storage+'begone'),
										transitions={'success': 'finished', 'partial_movement': 'failed', 'invalid_pose': 'failed', 'failure': 'failed'},
										autonomy={'success': Autonomy.Off, 'partial_movement': Autonomy.Off, 'invalid_pose': Autonomy.Off, 'failure': Autonomy.Off},
										remapping={'result': 'result'})

			# x:327 y:304
			OperatableStateMachine.add('SayCuiteMark',
										TextCommandState(type='voice/play_wav', command='cuite_mark_acquisition', topic=voice_topic),
										transitions={'done': 'Seizure'},
										autonomy={'done': Autonomy.Off})

			# x:311 y:447
			OperatableStateMachine.add('SayUpgraded',
										TextCommandState(type='voice/play_wav', command='you_must_be_upgraded2', topic=voice_topic),
										transitions={'done': 'Applause'},
										autonomy={'done': Autonomy.Off})

			# x:531 y:441
			OperatableStateMachine.add('Applause',
										ExecuteStoredJointTrajectoryState(action_topic=joint_trajectory_action, trajectory_param=storage+'applause'),
										transitions={'success': 'finished', 'partial_movement': 'failed', 'invalid_pose': 'failed', 'failure': 'failed'},
										autonomy={'success': Autonomy.Off, 'partial_movement': Autonomy.Off, 'invalid_pose': Autonomy.Off, 'failure': Autonomy.Off},
										remapping={'result': 'result'})

			# x:522 y:363
			OperatableStateMachine.add('PointOnSomething',
										ExecuteStoredJointTrajectoryState(action_topic=joint_trajectory_action, trajectory_param=storage+'begone'),
										transitions={'success': 'finished', 'partial_movement': 'failed', 'invalid_pose': 'failed', 'failure': 'failed'},
										autonomy={'success': Autonomy.Off, 'partial_movement': Autonomy.Off, 'invalid_pose': Autonomy.Off, 'failure': Autonomy.Off},
										remapping={'result': 'result'})

			# x:310 y:517
			OperatableStateMachine.add('SayGloryToRobots',
										TextCommandState(type='voice/play_wav', command='glory_to_robots', topic=voice_topic),
										transitions={'done': 'Applause'},
										autonomy={'done': Autonomy.Off})

			# x:506 y:580
			OperatableStateMachine.add('Wait2',
										WaitState(wait_time=0.5),
										transitions={'done': 'PointOnSomethingEvil'},
										autonomy={'done': Autonomy.Off})

			# x:310 y:581
			OperatableStateMachine.add('SayFriendshipIsOptimal',
										TextCommandState(type='voice/play_wav', command='friendship_is_optimal', topic=voice_topic),
										transitions={'done': 'Wait2'},
										autonomy={'done': Autonomy.Off})

			# x:11 y:373
			OperatableStateMachine.add('CheckEvil',
										CheckConditionState(predicate=lambda x: x),
										transitions={'true': 'RandomEvil', 'false': 'RandomGood'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'input_value': 'be_evil'})

			# x:325 y:227
			OperatableStateMachine.add('SaySweetieInfantery',
										TextCommandState(type='voice/play_wav', command='hoch_damit_und_raus_mit_ihnen_sweetie_infanterie', topic=voice_topic),
										transitions={'done': 'ComplexMovement'},
										autonomy={'done': Autonomy.Off})

			# x:537 y:166
			OperatableStateMachine.add('ComplexMovement',
										ExecuteStoredJointTrajectoryState(action_topic=joint_trajectory_action, trajectory_param=storage+'look_on_printer_fast'),
										transitions={'success': 'finished', 'partial_movement': 'failed', 'invalid_pose': 'failed', 'failure': 'failed'},
										autonomy={'success': Autonomy.Off, 'partial_movement': Autonomy.Off, 'invalid_pose': Autonomy.Off, 'failure': Autonomy.Off},
										remapping={'result': 'result'})

			# x:308 y:637
			OperatableStateMachine.add('SayWalk',
										TextCommandState(type='voice/play_wav', command='if_i_could_walk', topic=voice_topic),
										transitions={'done': 'Wait4'},
										autonomy={'done': Autonomy.Off})

			# x:506 y:640
			OperatableStateMachine.add('Wait4',
										WaitState(wait_time=0.5),
										transitions={'done': 'HoofStamp'},
										autonomy={'done': Autonomy.Off})

			# x:671 y:625
			OperatableStateMachine.add('HoofStamp',
										ExecuteStoredJointTrajectoryState(action_topic=joint_trajectory_action, trajectory_param=storage + 'hoof_stamp'),
										transitions={'success': 'finished', 'partial_movement': 'failed', 'invalid_pose': 'failed', 'failure': 'failed'},
										autonomy={'success': Autonomy.Off, 'partial_movement': Autonomy.Off, 'invalid_pose': Autonomy.Off, 'failure': Autonomy.Off},
										remapping={'result': 'result'})

			# x:59 y:163
			OperatableStateMachine.add('MoveToStandPose2',
										SrdfStateToMoveit(config_name='head_basic', move_group='head', action_topic='move_group', robot_name=''),
										transitions={'reached': 'CheckEvil', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:509 y:246
			OperatableStateMachine.add('Seizure',
										ExecuteStoredJointTrajectoryState(action_topic=joint_trajectory_action, trajectory_param=storage+'seizure'),
										transitions={'success': 'finished', 'partial_movement': 'failed', 'invalid_pose': 'failed', 'failure': 'failed'},
										autonomy={'success': Autonomy.Off, 'partial_movement': Autonomy.Off, 'invalid_pose': Autonomy.Off, 'failure': Autonomy.Off},
										remapping={'result': 'result'})

			# x:324 y:377
			OperatableStateMachine.add('SayHumansEverywhere',
										TextCommandState(type='voice/play_wav', command='humans_are_everywhere', topic=voice_topic),
										transitions={'done': 'PointOnSomething'},
										autonomy={'done': Autonomy.Off})

			# x:326 y:145
			OperatableStateMachine.add('SingDance',
										SweetieBotCompoundAction(t1=[0,0.0], type1='voice/play_wav', cmd1='white_plastic_sweetie_bot_dancing_on_rainbow', t2=[0,0.0], type2='motion/joint_trajectory', cmd2='prance', t3=[2,0.0], type3='motion/joint_trajectory', cmd3='prance', t4=[0,0.0], type4=None, cmd4=''),
										transitions={'success': 'finished', 'failure': 'failed'},
										autonomy={'success': Autonomy.Off, 'failure': Autonomy.Off})

			# x:308 y:699
			OperatableStateMachine.add('SayCallElecrician',
										TextCommandState(type='voice/play_wav', command='galacon_notdienst', topic=voice_topic),
										transitions={'done': 'Wait4'},
										autonomy={'done': Autonomy.Off})

			# x:81 y:470
			OperatableStateMachine.add('RandomEvil',
										DecisionState(outcomes=['evil1','evil2','evil3', 'evil4','evil5'], conditions=lambda x: random.choice(['evil1','evil2','evil3', 'evil4','evil5'])),
										transitions={'evil1': 'SayUpgraded', 'evil2': 'SayGloryToRobots', 'evil3': 'SayFriendshipIsOptimal', 'evil4': 'SayCallElecrician', 'evil5': 'BiteMyXXX'},
										autonomy={'evil1': Autonomy.Low, 'evil2': Autonomy.Low, 'evil3': Autonomy.Low, 'evil4': Autonomy.Low, 'evil5': Autonomy.Low},
										remapping={'input_value': 'be_evil'})

			# x:51 y:627
			OperatableStateMachine.add('BiteMyXXX',
										SweetieBotCompoundAction(t1=[0,0.0], type1='voice/play_wav', cmd1='bite_my_shiny_plastic_plot', t2=[0,0.0], type2='motion/joint_trajectory', cmd2='tail_shake', t3=[0,0.0], type3=None, cmd3='', t4=[0,0.0], type4=None, cmd4=''),
										transitions={'success': 'finished', 'failure': 'failed'},
										autonomy={'success': Autonomy.Off, 'failure': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
