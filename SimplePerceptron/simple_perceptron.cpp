#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

/* 訓練データの読み込み */
int train_data_load(const char *filename, vector<float> &x1, vector<float> &x2, vector<int> &label)
{
	FILE *fp;
	int i=0;
	int temp_label;
	float temp_x1, temp_x2;

	if((fp = fopen(filename, "r")) == NULL){
		cerr<<"open file faild."<<endl;
		return -1;
	}

	while(fscanf(fp, "%f %f %d", &temp_x1, &temp_x2, &temp_label) != EOF)
	{
		x1.push_back(temp_x1);
		x2.push_back(temp_x2);
		label.push_back(temp_label);
		i++;
	}
	return i;
}

/* シグモイド関数 */
float sigmoid(float x)
{
	return 1.0f / (1.0f + exp(-x));
}

/* シグモイド関数の微分 */
float sigmoid_dot(float x)
{
	return sigmoid(x)*(1.0f - sigmoid(x));
}

/* 誤差関数 */
float error_func(vector<float> x1, vector<float> x2, vector<int> label, float *w, const int data_num)
{
	float L=0.0;

	for(int i=0;i<data_num;i++)
		L += 0.5*pow((label[i]-sigmoid(x1[i]*w[0]+x2[i]*w[1])), 2);
	
	return L;
}

/* 重みベクトルの学習 */
void learning(vector<float> x1, vector<float> x2, vector<int> label, float &w1, float &w2, float *w_old, const int data_num, const int alpha=0.1)
{
	float w_new[2] = {0.0f, 0.0f};

	for(int i=0;i<data_num; i++){
		float x[2] = {x1[i], x2[i]};
		float wx=0.0;
		wx  = x1[i]*w_old[0] + x2[i]*w_old[1];
		for(int j=0;j<2;j++)
			w_new[j] = w_old[j] - alpha*(label[i]-sigmoid(wx))*sigmoid_dot(wx)*x[j];
	}
	w1 = w_new[0];
	w2 = w_new[1];
}

int main(int argc, char *argv[])
{
	vector<float> x1, x2;
	vector<int> label;
	float w_old[2] = {0.5, 0.2};
	float w[2];
	const int ITERATION=10;
	
	/* 訓練データのロード */
	const int data_num = train_data_load("input.txt", x1, x2, label);

	/* 重みベクトルの学習 */
	for(int i=0;i<ITERATION;i++){
		learning(x1, x2, label, w[0], w[1], w_old, data_num);
		for(size_t i=0;i<2;i++)
			w_old[i] = w[i];
		cout<<w[0]<<" "<<w[1]<<endl; 

		float L=0.0f;
		L = error_func(x1, x2, label, w, data_num);
		//cout<<"error:"<<L<<endl;
	}

	return 0;
}
