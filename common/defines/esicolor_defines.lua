NDefines.NGame.HANDS_OFF_START_TAG = "FIE"

NDefines.NDiplomacy.WARGOAL_PER_JUSTIFY_AND_WAR_COST_FACTOR = 1.3	-- Cost factor per nation at war with or justifying against

NDefines.NDiplomacy.PEACE_SCORE_DISTRIBUTION = { 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2 } -- How much of the total peace conference score you get during the first n turns.
NDefines.NDiplomacy.PEACE_CONTEST_REFUND_FACTOR = { 1.0, 0.90, 0.80, 0.70, 0.60, 0.50 } -- How much of the spent peace conference score that gets refunded in a contest. First element applies for the first round of conflicts, second element for the second round of conflicts, etc. The final element is used for each consecutive turn, so setting that to e.g. 0.7 means you get 70 % of the spent score back for every turn thereafter.

NDefines.NFactions.FACTION_INTELLIGENCE_ALLOWED_ADVISOR_TRAIT = {
	-- Basegame
	"head_of_intelligence",
	"mastermind_code_cracker",
	"expert_code_cracker",
	"spymaster",
	"spymaster_no_lar",
	"commander_of_the_fetno_derash",
	"commander_of_the_fetno_derash_no_lar",
	"SWI_soviet_spy",
	"SWI_intelligence_officer",
	"special_envoy",
	"BRA_soviet_spy",
	"HUN_military_intelligence_officer",
	"AUS_secretive_priest",
	"AUS_veteran_head_of_agency",
	"BEL_illusive_mastermind",
	"GER_intelligence_coordinator",
	"GER_secretary_of_state_security",
	"GER_reich_security_main_office_director_lar",
	"GER_reich_security_main_office_director_no_lar",
	"head_of_the_abwehr",
	"head_of_the_abwehr_improved",
	"intelligence_service_deputy",
	"PRC_multi_talented_diplomat_lar",
	"PRC_multi_talented_diplomat_no_lar",
	"PRC_trained_by_the_nkvd",
	"PRC_spymaster",
	"PHI_intelligence_bureau_chief",
	"HUN_stalinist_agent",
	"JAP_tokko_chief",
	"CHI_spymaster"

	-- ESI
	"code_breaker"
	"encryption_expert"
}
