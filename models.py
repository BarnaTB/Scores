class Scores:
    scores_dict = {}
    def validate_scores(self,cand_id,score):
        '''this method validates the user score input '''
        try:
            score = int(input("enter score mark: "))
            if score >= -2 and score <= 2:
                print("The value is out of range, try again.")
            else:
                for key in Scores.scores_dict:
                    if key == cand_id:
                        score.candidates_dict[cand_id] = score
                        print('score has been added successfully')
                    else:
                        print('user_id cannot be found')
        except ValueError:
            print("score mark should be an integer")

        	



     

    

	
		
		