# k-step-PIC
## "A Fast and Scalable Algorithm for Prior Art Search"
[`see more`](https://doi.org/10.1109/ACCESS.2022.3141494)

## Installation

`pip install git+https://github.com/lee-ju/k_step_pic.git`

## Usage

#### Load Package
```python
from k_step_pic import k_step_pic_E
```

#### Example Data
```python
from_cam = ['P1', 'P1', 'P2', 'P2', 'P3', 'P3', 'P4', 'P7', 'P8', 'P10']
to_cam = ['P2', 'P4', 'P3', 'P7', 'P4', 'P6', 'P5', 'P8', 'P9', 'P9']
from_sam = ['P1', 'P1', 'P1', 'P1', 'P1']
to_sam = ['P3', 'P5', 'P6', 'P9', 'P10']
repo = {'P1': 20050101,
        'P2': 20070101,
        'P3': 20100101,
        'P4': 20150101,
        'P5': 20200101,
        'P6': 20150101,
        'P7': 20100101,
        'P8': 20150101,
        'P9': 20200101,
        'P10': 20150101}
```
- `from_cam` and `to_cam` meaning:
    1. `from_cam`: In-node lists of Citation Network.
    2. `to_cam`: Out-node lists of Citation Network.

- `from_sam` and `to_sam` meaning:
    1. `from_sam`: In-node lists of Similarity Network.
    2. `to_sam`: Out-node lists of Similarity Network.

- `repo` meaning:
    1. `repo`: Dictionary containing the registration date of each patent.
<img src="/imgs/fig-example.png" width="400" height="300">

#### one-step PIC
```python
k = 1
results = k_step_pic_E(from_cam=from_cam, to_cam=to_cam,
                       from_sam=from_sam, to_sam=to_sam,
                       repo=repo, td_max=365*20, k=k)
print("* * one-step-PIC * * \n", results, "\n")
```

```python
[Out]: 
* * one-step-PIC * * 
   P_E P_L
0  P1  P3
1  P1  P5 
```
<img src="/imgs/fig-1step.png" width="400" height="300">

#### two-step PIC
```python
k = 2
results = k_step_pic_E(from_cam=from_cam, to_cam=to_cam,
                       from_sam=from_sam, to_sam=to_sam,
                       repo=repo, td_max=365*20, k=k)
print("* * two-step-PIC * * \n", results, "\n")
```

```python
[Out]: 
* * two-step-PIC * * 
   P_E P_L
0  P1  P6 
```
<img src="/imgs/fig-2step.png" width="400" height="300">

#### three-step PIC
```python
k = 3
results = k_step_pic_E(from_cam=from_cam, to_cam=to_cam,
                       from_sam=from_sam, to_sam=to_sam,
                       repo=repo, td_max=365*20, k=k)
print("* * three-step-PIC * * \n", results, "\n")
```

```python
[Out]: 
* * three-step-PIC * * 
   P_E P_L
0  P1  P9 
```
<img src="/imgs/fig-3step.png" width="400" height="300">

## Parameters

#### `k_step_PIC`
- `k_step_pic_E` constructor:
    1. `from_cam`: In-node lists of Citation Network. (default: None)
    2. `to_cam`: Out-node lists of Citation Network. (default: None)
    3. `from_sam`: In-node lists of Similarity Network. (default: None)
    4. `to_sam`: Out-node lists of Similarity Network. (default: None)
    5. `repo`: Dictionary containing the registration date of each patent. (default: None)
    6. `td_max`: Maximum difference in registration dates. The range is 0 to 7300 (days). (default: None)
    7. `k`: Number of steps. (default: 1)
