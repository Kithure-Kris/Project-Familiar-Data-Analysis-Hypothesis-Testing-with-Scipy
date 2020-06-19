import familiar
from scipy.stats import ttest_1samp, ttest_ind, chi2_contingency
vein_pack_lifespans = familiar.lifespans(package='vein')

#What Can Familiar Do For You?
ttest, vein_pack_test = ttest_1samp(vein_pack_lifespans, 71)
print vein_pack_test

if (vein_pack_test<0.05):
  print 'The Vein Pack Is Proven To Make You Live Longer!'
else:
  print 'The Vein Pack Is Probably Good For You Somehow!'

#Comparing Lifespan data between our different packages.
artery_pack_lifespans = familiar.lifespans(package='artery')

ttest, package_comparison_results = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
print package_comparison_results

if (package_comparison_results<0.05):
  print 'the Artery Package guarantees even stronger results!'
else:
  print 'the Artery Package is also a great product!'

#Comparing iron count between the various subscribers from a survey
iron_contingency_table = familiar.iron_counts_for_package()

chi2, iron_pvalue, dof, expected = chi2_contingency(iron_contingency_table)
print iron_pvalue

if (iron_pvalue<0.05):
  print 'The Artery Package Is Proven To Make You Healthier!'
else:
  print "While We Can't Say The Artery Package Will Help You, I Bet It's Nice!"