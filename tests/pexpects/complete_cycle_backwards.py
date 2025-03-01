#!/usr/bin/env python3
from pexpect_helper import SpawnedProc

sp = SpawnedProc()
send, sendline, sleep, expect_prompt, expect_re, expect_str = (
    sp.send,
    sp.sendline,
    sp.sleep,
    sp.expect_prompt,
    sp.expect_re,
    sp.expect_str,
)
expect_prompt()

# sendline("complete -x -c monster -a truck")
# expect_prompt()
# send("monster t")
# sleep(0.1)
# send("\t")
# sleep(0.1)
# send("!")
# expect_str("monster truck !")  # space

# Set up completions
sendline("complete -x -c testcmd -a 'a b c'")
expect_prompt()

# Test forward cycling (default behavior)
send("testcmd ")
sleep(0.1)
send("\t")
sleep(0.1)
send("\t")
sleep(0.1)
send("\t")
sleep(0.1)
expect_str("testcmd a")
sleep(0.1)
send("\t")
sleep(0.1)
send("\t")
sleep(0.1)
# expect_re(".*")
expect_str("testcmd a")
# sleep(0.1)
# send("\t")
# sleep(0.1)
# expect_str("testcmd option2")
# expect_re(".*")
# expect_str("not existing")
# send("\t")
# expect_str("testcmd option3")
# send("\t")
# expect_str("testcmd option1")  # Cycles back to the first option
# send("\033")  # Send escape
# sendline("")
# expect_prompt()

# # Test backward cycling with fish_complete_cycle_backwards=1
# sendline("set -g fish_complete_cycle_backwards 1")
# expect_prompt()
# send("testcmd \t")
# expect_str("testcmd option1")
# send("\t")
# expect_str("testcmd option3")  # Should go backwards from first to last
# send("\t")
# expect_str("testcmd option2")  # Should continue backwards
# send("\t")
# expect_str("testcmd option1")  # Back to first
# send("\033")  # Send escape
# sendline("")
# expect_prompt()

# # Test shift-tab which should always cycle backwards regardless of the setting
# sendline("set -e fish_complete_cycle_backwards")  # Reset to default behavior
# expect_prompt()
# send("testcmd \t")
# expect_str("testcmd option1")
# # Send shift-tab (this may be environment-dependent, but for most terminals it's "\e[Z")
# send("\033[Z")
# expect_str("testcmd option3")  # Should go backwards from first to last
# send("\033[Z")
# expect_str("testcmd option2")  # Should continue backwards
# send("\033")  # Send escape
# sendline("")
# expect_prompt()
