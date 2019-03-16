# -*- coding: utf-8 -*-

print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'


# 读不懂的小诗 <_<|||
# 以下为有道词典的机器翻译，供参考
# --- 这可爱的世界
# --- 有着如此牢固的逻辑根基
# --- 无法分辨爱的需要
# --- 也不能凭直觉理解激情
# --- 需要一个解释
# --- 在没有爱的地方。
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

print "-------------------------"
print poem
print "-------------------------"


five = 10 - 2 + 3 -6
print "This should be five: %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting piont of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

