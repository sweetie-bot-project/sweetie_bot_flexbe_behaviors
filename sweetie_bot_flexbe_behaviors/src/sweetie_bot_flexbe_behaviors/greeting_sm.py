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
from sweetie_bot_flexbe_states.execute_stored_trajectory_state import ExecuteStoredJointTrajectoryState
from sweetie_bot_flexbe_states.text_command_state import TextCommandState
from flexbe_states.decision_state import DecisionState
from flexbe_states.wait_state import WaitState
from sweetie_bot_flexbe_states.sweetie_bot_compound_action_state import SweetieBotCompoundAction
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]
import random
# [/MANUAL_IMPORT]


'''
Created on Tue Mar 28 2017
@author: disRecord
'''
class GreetingSM(Behavior):
	'''
	SweetieBot greeting behavior.
	'''


	def __init__(self):
		super(GreetingSM, self).__init__()
		self.name = 'Greeting'

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
		# x:1044 y:507, x:1035 y:15
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['be_evil'])
		_state_machine.userdata.be_evil = self.be_evil

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:37 y:189
			OperatableStateMachine.add('MoveStandPose',
										SrdfStateToMoveit(config_name='head_basic', move_group='head', action_topic='move_group', robot_name=''),
										transitions={'reached': 'RandomChoose', 'planning_failed': 'MoveToStandPose2', 'control_failed': 'MoveToStandPose2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:507 y:53
			OperatableStateMachine.add('IntroduceHerself',
										ExecuteStoredJointTrajectoryState(action_topic=joint_trajectory_action, trajectory_param=storage + 'introduce_herself'),
										transitions={'success': 'finished', 'partial_movement': 'failed', 'invalid_pose': 'failed', 'failure': 'failed'},
										autonomy={'success': Autonomy.Off, 'partial_movement': Autonomy.Off, 'invalid_pose': Autonomy.Off, 'failure': Autonomy.Off},
										remapping={'result': 'result'})

			# x:318 y:135
			OperatableStateMachine.add('SayInitAcquitance',
										TextCommandState(type='voice/play_wav', command='do_you_want_brohoof', topic=voice_topic),
										transitions={'done': 'BrohoofBegin'},
										autonomy={'done': Autonomy.Off})

			# x:471 y:130
			OperatableStateMachine.add('BrohoofBegin',
										ExecuteStoredJointTrajectoryState(action_topic=joint_trajectory_action, trajectory_param=storage+'brohoof_begin'),
										transitions={'success': 'Wait2', 'partial_movement': 'failed', 'invalid_pose': 'failed', 'failure': 'failed'},
										autonomy={'success': Autonomy.Off, 'partial_movement': Autonomy.Off, 'invalid_pose': Autonomy.Off, 'failure': Autonomy.Off},
										remapping={'result': 'result'})

			# x:500 y:685
			OperatableStateMachine.add('Rejection',
										ExecuteStoredJointTrajectoryState(action_topic=joint_trajectory_action, trajectory_param=storage+'begone'),
										transitions={'success': 'finished', 'partial_movement': 'failed', 'invalid_pose': 'failed', 'failure': 'failed'},
										autonomy={'success': Autonomy.Off, 'partial_movement': Autonomy.Off, 'invalid_pose': Autonomy.Off, 'failure': Autonomy.Off},
										remapping={'result': 'result'})

			# x:504 y:214
			OperatableStateMachine.add('HeadSuprised',
										ExecuteStoredJointTrajectoryState(action_topic=joint_trajectory_action, trajectory_param=storage+'head_suprised'),
										transitions={'success': 'finished', 'partial_movement': 'failed', 'invalid_pose': 'failed', 'failure': 'failed'},
										autonomy={'success': Autonomy.Off, 'partial_movement': Autonomy.Off, 'invalid_pose': Autonomy.Off, 'failure': Autonomy.Off},
										remapping={'result': 'result'})

			# x:320 y:218
			OperatableStateMachine.add('SayQuestion',
										TextCommandState(type='voice/play_wav', command='do_you_dream_of_robot_ponies', topic=voice_topic),
										transitions={'done': 'HeadSuprised'},
										autonomy={'done': Autonomy.Off})

			# x:292 y:688
			OperatableStateMachine.add('SayDoYouWantMyAttention',
										TextCommandState(type='voice/play_wav', command='do_you_want_my_attention', topic=voice_topic),
										transitions={'done': 'Rejection'},
										autonomy={'done': Autonomy.Off})

			# x:317 y:48
			OperatableStateMachine.add('SayImRedyForCon',
										TextCommandState(type='voice/play_wav', command='conbereitschatfsstufe1', topic=voice_topic),
										transitions={'done': 'IntroduceHerself'},
										autonomy={'done': Autonomy.Off})

			# x:745 y:675
			OperatableStateMachine.add('HoofStompRejection',
										ExecuteStoredJointTrajectoryState(action_topic=joint_trajectory_action, trajectory_param=storage + 'hoof_stamp'),
										transitions={'success': 'finished', 'partial_movement': 'failed', 'invalid_pose': 'failed', 'failure': 'failed'},
										autonomy={'success': Autonomy.Off, 'partial_movement': Autonomy.Off, 'invalid_pose': Autonomy.Off, 'failure': Autonomy.Off},
										remapping={'result': 'result'})

			# x:152 y:269
			OperatableStateMachine.add('RandomChoose',
										DecisionState(outcomes=['good1', 'good2', 'good3', 'good4', 'evil1', 'evil2', 'evil3', 'evil4'], conditions=lambda evil: random.choice(['good1', 'good2', 'good3', 'good4']) if not evil else random.choice(['evil1','evil2','evil3','evil4'])),
										transitions={'good1': 'SayImRedyForCon', 'good2': 'SayInitAcquitance', 'good3': 'SayQuestion', 'good4': 'SayCelestiaAI', 'evil1': 'AskAboutRocketLauncher', 'evil2': 'IllHugYouNeck', 'evil3': 'LasersBeamsDE', 'evil4': 'SayDoYouWantMyAttention'},
										autonomy={'good1': Autonomy.Low, 'good2': Autonomy.Low, 'good3': Autonomy.Low, 'good4': Autonomy.Low, 'evil1': Autonomy.Low, 'evil2': Autonomy.Low, 'evil3': Autonomy.Low, 'evil4': Autonomy.Low},
										remapping={'input_value': 'be_evil'})

			# x:40 y:408
			OperatableStateMachine.add('MoveToStandPose2',
										SrdfStateToMoveit(config_name='head_basic', move_group='head', action_topic='move_group', robot_name=''),
										transitions={'reached': 'RandomChoose', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:690 y:126
			OperatableStateMachine.add('Wait2',
										WaitState(wait_time=3),
										transitions={'done': 'BrohoofEnd'},
										autonomy={'done': Autonomy.Off})

			# x:792 y:131
			OperatableStateMachine.add('BrohoofEnd',
										ExecuteStoredJointTrajectoryState(action_topic=joint_trajectory_action, trajectory_param=storage+'brohoof_end'),
										transitions={'success': 'finished', 'partial_movement': 'failed', 'invalid_pose': 'failed', 'failure': 'failed'},
										autonomy={'success': Autonomy.Off, 'partial_movement': Autonomy.Off, 'invalid_pose': Autonomy.Off, 'failure': Autonomy.Off},
										remapping={'result': 'result'})

			# x:324 y:277
			OperatableStateMachine.add('SayCelestiaAI',
										TextCommandState(type='voice/play_wav', command='celest_ai_is_coming', topic=voice_topic),
										transitions={'done': 'Greeting'},
										autonomy={'done': Autonomy.Off})

			# x:502 y:280
			OperatableStateMachine.add('Greeting',
										ExecuteStoredJointTrajectoryState(action_topic=joint_trajectory_action, trajectory_param=storage+'greeting'),
										transitions={'success': 'finished', 'partial_movement': 'failed', 'invalid_pose': 'failed', 'failure': 'failed'},
										autonomy={'success': Autonomy.Off, 'partial_movement': Autonomy.Off, 'invalid_pose': Autonomy.Off, 'failure': Autonomy.Off},
										remapping={'result': 'result'})

			# x:378 y:384
			OperatableStateMachine.add('AskAboutRocketLauncher',
										SweetieBotCompoundAction(t1=[0,0.0], type1='motion/joint_trajectory', cmd1='lean_forward_begin', t2=[1,0.0], type2='voice/play_wav', cmd2='do_you_have_any_blueprins_of_missle_launchers', t3=[1,5.0], type3='motion/joint_trajectory', cmd3='lean_forward_end', t4=[1,0.0], type4='motion/joint_trajectory', cmd4='head_suprised_slow'),
										transitions={'success': 'finished', 'failure': 'failed'},
										autonomy={'success': Autonomy.Off, 'failure': Autonomy.Off})

			# x:383 y:455
			OperatableStateMachine.add('IllHugYouNeck',
										SweetieBotCompoundAction(t1=[0,0.0], type1='voice/play_wav', cmd1='ill_hug_your_neck', t2=[0,0.0], type2='motion/joint_trajectory', cmd2='begone', t3=[0,0.0], type3=None, cmd3='', t4=[0,0.0], type4=None, cmd4=''),
										transitions={'success': 'finished', 'failure': 'failed'},
										autonomy={'success': Autonomy.Off, 'failure': Autonomy.Off})

			# x:582 y:514
			OperatableStateMachine.add('ControlYou',
										SweetieBotCompoundAction(t1=[0,0.0], type1='voice/play_wav', cmd1='someday_ill_control_you', t2=[0,0.3], type2='motion/joint_trajectory', cmd2='begone', t3=[0,0.0], type3=None, cmd3='', t4=[0,0.0], type4=None, cmd4=''),
										transitions={'success': 'finished', 'failure': 'failed'},
										autonomy={'success': Autonomy.Off, 'failure': Autonomy.Off})

			# x:378 y:576
			OperatableStateMachine.add('LasersBeamsDE',
										SweetieBotCompoundAction(t1=[0,0.0], type1='voice/play_wav', cmd1='bestatige_canni_sweetie_bot_ubernimmt_nun_die_kontrolle', t2=[0,1.0], type2='motion/joint_trajectory', cmd2='menace', t3=[2,2.0], type3='motion/joint_trajectory', cmd3='menace_canceled', t4=[3,0.0], type4='voice/play_wav', cmd4='laseraugen_sind_nett_aber_hutet_euch_vor_cannis_bizaam'),
										transitions={'success': 'failed', 'failure': 'finished'},
										autonomy={'success': Autonomy.Off, 'failure': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
