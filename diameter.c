/* Helper function that allocates a new node with the
   given data and NULL left and right pointers. */
/* A binary tree node has data, pointer to left child
   and a pointer to right child */

#include <stdio.h>
#include <stdlib.h>
struct node{
    int data;
    struct node* left;
    struct node* right;
};
 
/* function to create a new node of tree and returns pointer */
struct node* newNode(int data);
 
/* returns max of two integers */
int max(int a, int b);
 
/* function to Compute height of a tree. */
int height(struct node* node);

/* returns maximum of two integers */
int max(int a, int b){
  return (a >= b)? a: b;
}   

struct node* newNode(int data){
  struct node* node = (struct node*) malloc(sizeof(struct node));
  node->data = data;
  node->left = NULL;
  node->right = NULL;
 
  return(node);
}

/*The second parameter is to store the height of tree.
   Initially, we need to pass a pointer to a location with value
   as 0. So, function should be used as follows:
 
   int height = 0;
   struct node *root = SomeFunctionToMakeTree();
   int diameter = diameterOpt(root, &height); */
int diameterOpt(struct node *root, int* height)
{
  /* lh --> Height of left subtree
      rh --> Height of right subtree */
  int lh = 0, rh = 0;
  
  /* ldiameter  --> diameter of left subtree
      rdiameter  --> Diameter of right subtree */
  int ldiameter = 0, rdiameter = 0;
  
  if(root == NULL) {
    *height = 0;
     return 0; /* diameter is also 0 */
  }
  
  /* Get the heights of left and right subtrees in lh and rh
    And store the returned values in ldiameter and ldiameter */
  ldiameter = diameterOpt(root->left, &lh);
  rdiameter = diameterOpt(root->right, &rh);
  
  /* Height of current node is max of heights of left and
     right subtrees plus 1*/
  *height = max(lh, rh) + 1;
  
  return max(lh + rh + 1, max(ldiameter, rdiameter));
}

/* Driver program to test above functions*/
int main()
{
 
  /* Constructed binary tree is 
            1
          /   \
        2      3
      /  \
    4     5
  */
  struct node *root = newNode(1);
  root->left        = newNode(2);
  root->right       = newNode(3);
  root->left->left  = newNode(4);
  root->left->right = newNode(5);
 
  int height = 0;
  printf("Diameter of the given binary tree is %d\n", diameterOpt(root, &height));
 
  return 0;
}
