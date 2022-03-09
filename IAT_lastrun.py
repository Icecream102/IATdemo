#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.1),
    on 三月 08, 2022, at 21:14
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.1'
expName = 'IAT'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\vscode\\codes\\pycodes\\IAT\\IAT_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "preBlockInstr"
preBlockInstrClock = core.Clock()
preBlockInstr_image = visual.ImageStim(
    win=win,
    name='preBlockInstr_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.75, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
preBlockInstr_key = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
label_left = visual.ImageStim(
    win=win,
    name='label_left', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0.4), size=(0.3, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
label_right = visual.ImageStim(
    win=win,
    name='label_right', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.4, 0.4), size=(0.3, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
fixation = visual.ShapeStim(
    win=win, name='fixation', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='red',
    opacity=0.0, depth=-2.0, interpolate=True)
stim = visual.ImageStim(
    win=win,
    name='stim', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "endBlockInstr"
endBlockInstrClock = core.Clock()
endBlockInstr_image = visual.ImageStim(
    win=win,
    name='endBlockInstr_image', 
    image='endBlockInstr.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.75, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
endBlockInstr_key = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('IAT_block_loop.xlsx'),
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "preBlockInstr"-------
    continueRoutine = True
    # update component parameters for each repeat
    preBlockInstr_image.setImage(InstrImage)
    preBlockInstr_key.keys = []
    preBlockInstr_key.rt = []
    _preBlockInstr_key_allKeys = []
    # keep track of which components have finished
    preBlockInstrComponents = [preBlockInstr_image, preBlockInstr_key]
    for thisComponent in preBlockInstrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    preBlockInstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "preBlockInstr"-------
    while continueRoutine:
        # get current time
        t = preBlockInstrClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=preBlockInstrClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *preBlockInstr_image* updates
        if preBlockInstr_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            preBlockInstr_image.frameNStart = frameN  # exact frame index
            preBlockInstr_image.tStart = t  # local t and not account for scr refresh
            preBlockInstr_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(preBlockInstr_image, 'tStartRefresh')  # time at next scr refresh
            preBlockInstr_image.setAutoDraw(True)
        
        # *preBlockInstr_key* updates
        waitOnFlip = False
        if preBlockInstr_key.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            preBlockInstr_key.frameNStart = frameN  # exact frame index
            preBlockInstr_key.tStart = t  # local t and not account for scr refresh
            preBlockInstr_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(preBlockInstr_key, 'tStartRefresh')  # time at next scr refresh
            preBlockInstr_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(preBlockInstr_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(preBlockInstr_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if preBlockInstr_key.status == STARTED and not waitOnFlip:
            theseKeys = preBlockInstr_key.getKeys(keyList=['space'], waitRelease=False)
            _preBlockInstr_key_allKeys.extend(theseKeys)
            if len(_preBlockInstr_key_allKeys):
                preBlockInstr_key.keys = _preBlockInstr_key_allKeys[-1].name  # just the last key pressed
                preBlockInstr_key.rt = _preBlockInstr_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in preBlockInstrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "preBlockInstr"-------
    for thisComponent in preBlockInstrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blocks.addData('preBlockInstr_image.started', preBlockInstr_image.tStartRefresh)
    blocks.addData('preBlockInstr_image.stopped', preBlockInstr_image.tStopRefresh)
    # the Routine "preBlockInstr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    SingleBlock = data.TrialHandler(nReps=reps, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(block_loop),
        seed=None, name='SingleBlock')
    thisExp.addLoop(SingleBlock)  # add the loop to the experiment
    thisSingleBlock = SingleBlock.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSingleBlock.rgb)
    if thisSingleBlock != None:
        for paramName in thisSingleBlock:
            exec('{} = thisSingleBlock[paramName]'.format(paramName))
    
    for thisSingleBlock in SingleBlock:
        currentLoop = SingleBlock
        # abbreviate parameter names if possible (e.g. rgb = thisSingleBlock.rgb)
        if thisSingleBlock != None:
            for paramName in thisSingleBlock:
                exec('{} = thisSingleBlock[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        label_left.setImage(leftLabel)
        label_right.setImage('rightLabel')
        stim.setImage(stims)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        trialComponents = [label_left, label_right, fixation, stim, key_resp]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *label_left* updates
            if label_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                label_left.frameNStart = frameN  # exact frame index
                label_left.tStart = t  # local t and not account for scr refresh
                label_left.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(label_left, 'tStartRefresh')  # time at next scr refresh
                label_left.setAutoDraw(True)
            
            # *label_right* updates
            if label_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                label_right.frameNStart = frameN  # exact frame index
                label_right.tStart = t  # local t and not account for scr refresh
                label_right.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(label_right, 'tStartRefresh')  # time at next scr refresh
                label_right.setAutoDraw(True)
            
            # *fixation* updates
            if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                fixation.setAutoDraw(True)
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                    fixation.setAutoDraw(False)
            
            # *stim* updates
            if stim.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                stim.frameNStart = frameN  # exact frame index
                stim.tStart = t  # local t and not account for scr refresh
                stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim, 'tStartRefresh')  # time at next scr refresh
                stim.setAutoDraw(True)
            
            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['e','i'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # was this correct?
                    if (key_resp.keys == str(correct_key)) or (key_resp.keys == correct_key):
                        key_resp.corr = 1
                    else:
                        key_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        SingleBlock.addData('label_left.started', label_left.tStartRefresh)
        SingleBlock.addData('label_left.stopped', label_left.tStopRefresh)
        SingleBlock.addData('label_right.started', label_right.tStartRefresh)
        SingleBlock.addData('label_right.stopped', label_right.tStopRefresh)
        SingleBlock.addData('fixation.started', fixation.tStartRefresh)
        SingleBlock.addData('fixation.stopped', fixation.tStopRefresh)
        SingleBlock.addData('stim.started', stim.tStartRefresh)
        SingleBlock.addData('stim.stopped', stim.tStopRefresh)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
            # was no response the correct answer?!
            if str(correct_key).lower() == 'none':
               key_resp.corr = 1;  # correct non-response
            else:
               key_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for SingleBlock (TrialHandler)
        SingleBlock.addData('key_resp.keys',key_resp.keys)
        SingleBlock.addData('key_resp.corr', key_resp.corr)
        if key_resp.keys != None:  # we had a response
            SingleBlock.addData('key_resp.rt', key_resp.rt)
        SingleBlock.addData('key_resp.started', key_resp.tStartRefresh)
        SingleBlock.addData('key_resp.stopped', key_resp.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed reps repeats of 'SingleBlock'
    
    
    # ------Prepare to start Routine "endBlockInstr"-------
    continueRoutine = True
    # update component parameters for each repeat
    endBlockInstr_key.keys = []
    endBlockInstr_key.rt = []
    _endBlockInstr_key_allKeys = []
    # keep track of which components have finished
    endBlockInstrComponents = [endBlockInstr_image, endBlockInstr_key]
    for thisComponent in endBlockInstrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    endBlockInstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "endBlockInstr"-------
    while continueRoutine:
        # get current time
        t = endBlockInstrClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=endBlockInstrClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *endBlockInstr_image* updates
        if endBlockInstr_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            endBlockInstr_image.frameNStart = frameN  # exact frame index
            endBlockInstr_image.tStart = t  # local t and not account for scr refresh
            endBlockInstr_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endBlockInstr_image, 'tStartRefresh')  # time at next scr refresh
            endBlockInstr_image.setAutoDraw(True)
        
        # *endBlockInstr_key* updates
        waitOnFlip = False
        if endBlockInstr_key.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            endBlockInstr_key.frameNStart = frameN  # exact frame index
            endBlockInstr_key.tStart = t  # local t and not account for scr refresh
            endBlockInstr_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endBlockInstr_key, 'tStartRefresh')  # time at next scr refresh
            endBlockInstr_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(endBlockInstr_key.clock.reset)  # t=0 on next screen flip
        if endBlockInstr_key.status == STARTED and not waitOnFlip:
            theseKeys = endBlockInstr_key.getKeys(keyList=['space'], waitRelease=False)
            _endBlockInstr_key_allKeys.extend(theseKeys)
            if len(_endBlockInstr_key_allKeys):
                endBlockInstr_key.keys = _endBlockInstr_key_allKeys[-1].name  # just the last key pressed
                endBlockInstr_key.rt = _endBlockInstr_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in endBlockInstrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "endBlockInstr"-------
    for thisComponent in endBlockInstrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blocks.addData('endBlockInstr_image.started', endBlockInstr_image.tStartRefresh)
    blocks.addData('endBlockInstr_image.stopped', endBlockInstr_image.tStopRefresh)
    # the Routine "endBlockInstr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'blocks'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
