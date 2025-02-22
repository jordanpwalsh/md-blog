# Tackling Complex Problems With a Problem Stack

Here is an approach to tackling complex and unknown problems - The problem stack. Recall that many computer architectures, languages, and runtimes use a call stack in order to enable things like memory management, exception handling, and recursion. The idea is simple: separate out problems into distinct and manageable chunks of work based on their dependency to other problems. Take this example task:

**Update Splunk side car to latest version**

Simple enough but all too often we run into an issue preventing us from cleanly updating to the latest sidecar version, maybe the deployment is failing. That needs to be fixed first, but we don't want to lose track of our initial goal. Enter the problem stack. Once you recognize you in a cascading set of problems, pick a problem and keep track of its relation to others.

**Update Splunk side car to latest version**
- Fix deployment
	- SSL cert automation is broken - need to fix first.

In this case the automation generating our SSL certs is broken. Take a step into the stack and solve that problem first, bubbling up the stack as each subsequent problem is resolved. 

**Update Splunk side car to latest version**
- Fix deployment
	- SSL cert automation is broken - need to fix first.
		- python dependency is 404ing from Pip.

As the dependent problems begin to be solved and solutions bubble up the stack, removing blockers to the original issue while keeping track of steady progress.


